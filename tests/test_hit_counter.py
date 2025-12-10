import pytest

from src.hit_counter import HitCounter, HitCounterBucket


test_data = [
    ([], 3, 0),
    ([1, 2, 3, 301], 300, 3),
    ([1, 2, 3, 301], 301, 3),
    ([1, 2, 3, 301], 500, 1),
    ([1, 2, 3, 301], 700, 0),
    ([1, 1, 2, 2, 2, 3, 301], 300, 6)
]

@pytest.mark.parametrize("hits, timestamp, expected", test_data)
def test_hit_counter(hits, timestamp, expected):
    counter = HitCounter()
    for hit in hits:
        counter.hit(hit)
    assert counter.getHits(timestamp) == expected

@pytest.mark.parametrize("hits, timestamp, expected", test_data)
def test_hit_counter_bucket(hits, timestamp, expected):
    counter = HitCounterBucket()
    for hit in hits:
        counter.hit(hit)
    assert counter.getHits(timestamp) == expected
