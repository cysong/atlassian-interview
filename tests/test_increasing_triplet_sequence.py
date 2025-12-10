import pytest
from src.increasing_triplet_sequence import Solution


test_data = [
    ([1,2,3,4,5], True),
    ([5,4,3,2,1], False),
    ([2,1,5,0,4,6], True),
    ([1,1,-2,5], False)
]

@pytest.mark.parametrize("nums, expected", test_data)
def test(nums: list[int], expected:bool):
    assert Solution().increasingTriplet(nums) == expected