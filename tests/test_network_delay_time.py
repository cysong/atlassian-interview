import pytest
from src.network_delay_time import Solution

test_data = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1),
    ([[1,2,1]], 2, 2, -1)
]

@pytest.mark.parametrize("times, n, k, expected", test_data)
def test_network_delay_time(times, n, k, expected):
    assert Solution().networkDelayTime(times, n, k) == expected

@pytest.mark.parametrize("times, n, k, expected", test_data)
def test_network_delay_time_dijkstra(times, n, k, expected):
    assert Solution().networkDelayTime(times, n, k) == expected

