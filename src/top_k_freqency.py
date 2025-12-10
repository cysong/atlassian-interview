# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List


class Solution:
    def heap(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        import heapq
        heap = []
        for key, freq in frequency.items():
            heapq.heappush(heap, (-freq, key))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

    def bucket(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for key, freq in frequency.items():
            buckets[freq].append(key)

        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result