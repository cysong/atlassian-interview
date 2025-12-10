import pytest
from src.merge_intervals import Solution

test_data = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[4,7],[1,4]], [[1,7]])
]


@pytest.mark.parametrize("intervals, expected", test_data)
def test_intervals_merge(intervals, expected):
    assert Solution().merge(intervals) == expected