from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # sort interval by the first number
        intervals.sort(key=lambda interval: interval[0])

        # merge the adjacent overlaping interval
        merged = []
        current_interval = intervals[0]
        for next_interval in intervals[1:]:
            if current_interval[1] >= next_interval[0]:
                current_interval = [current_interval[0], max(current_interval[1], next_interval[1])]
            else:
                merged.append(current_interval)
                current_interval = next_interval
        merged.append(current_interval)

        return merged
