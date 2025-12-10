
from typing import List


class Solution():

    def increasingTriplet(self, nums: List[int]) -> bool:
        low, mid = float("inf"), float("inf")
        for num in nums:
            if num <= low:
                low = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False