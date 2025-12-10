from src.notification import Event, EventService
from src.two_sum import two_sum


def test_notific():
    eventser = EventService()
    event = Event()
    event.authors = ['anson', 'jack']
    event.event_type='DeploySuccess'
    event.version_no='1'
    eventser.handleEvent(event)

    event2 = event = Event()
    event2.authors = ['alice', 'bob']
    event2.event_type='DeployFail'
    event2.version_no='2'
    eventser.handleEvent(event2)



def test_two_sum_basic() -> None:
    """测试基本正向案例"""
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert two_sum(nums, target) == expected