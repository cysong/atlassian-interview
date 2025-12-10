
from os import times


class HitCounter:
    def __init__(self):
        self.window = 300
        self.history = []
        self.last_timestamp = -1

    def hit(self, timestamp: int) -> None:
        if timestamp == self.last_timestamp:
            self.history[-1][1] = self.history[-1][1] + 1
        else:
            self.history.append([timestamp, self.history[-1][1]+1 if self.history else 1])
            self.last_timestamp = timestamp

    def getHits(self, timestamp) -> int:
        high_index = self._find_last_le(timestamp)
        if high_index == -1:
            return 0  # 所有记录都在查询时间之后
        low_timestamp = timestamp - self.window
        # 查找 history 中时间戳 <= low_timestamp 的最大索引
        low_index = self._find_last_le(low_timestamp)
        if low_index == -1:
            # 窗口起点之前的没有记录，即所有记录都在窗口内
            return self.history[high_index][1]
        else:
            # 总数减去窗口起点之前的总数
            return self.history[high_index][1] - self.history[low_index][1]

    def _find_last_le(self, target_timestamp):
        # 查找 history 中时间戳 <= target_timestamp 的最大索引
        low, high = max(0, len(self.history) - self.window), len(self.history) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if self.history[mid][0] <= target_timestamp:
                result = mid  # 可能是答案，继续向右找
                low = mid + 1
            else:
                high = mid - 1  # 时间戳太大，向左找
        return result


class HitCounterBucket:
    def __init__(self) -> None:
        self.window = 300
        self.timestamps = [0] * self.window
        self.counter = [0] * self.window

    def hit(self, timestamp) -> None:
        index = timestamp % self.window
        if self.timestamps[index] == timestamp:
            self.counter[index] += 1
        else:
            self.timestamps[index] = timestamp
            self.counter[index] = 1

    def getHits(self, timestamp) -> int:
        low_timestamp = timestamp - self.window + 1
        result = 0
        for i in range(self.window):
            if self.timestamps[i] >= low_timestamp:
                result += self.counter[i]
        return result
