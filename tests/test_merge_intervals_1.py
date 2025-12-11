from src.merge_intervals_1 import Solution

import pytest


test_data = [
    ([(2, 5), (12, 15), (4, 8)], [(2, 8), (12, 15)]),
    ([],[]),
    ([(1,10), (2,3), (6,9)],[(1, 10)])
]


@pytest.mark.parametrize("input, expected", test_data)
def test_merge(input, expected):
    solution  = Solution(input)
    assert solution.merge() == expected
