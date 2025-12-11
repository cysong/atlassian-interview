from typing import List
from src.notification import Event, EventService, EventType, Message, NotificationSender


class FakeNotificationService(NotificationSender):
    def __init__(self) -> None:
        self.messages: List[Message] = []

    def send_message(self, message: Message) -> None:
        self.messages.append(message)

def test_deploy_fail_is_stored():
    notification = FakeNotificationService()
    service = EventService(notification)

    event = Event(EventType.DEPLOY_FAIL, "1.0.0", ["alice"])
    service.handleEvent(event)

    assert len(service.deploys) == 1
    assert service.deploys[0].version_no == "1.0.0"
    assert service.deploys[0].authors == ["alice"]

def test_deploy_success_sends_notifications_to_all_authors():
    notification = FakeNotificationService()
    service = EventService(notification)

    service.handleEvent(Event(EventType.DEPLOY_FAIL, "1.0.0", ["alice"]))
    service.handleEvent(Event(EventType.DEPLOY_FAIL, "1.0.1", ["bob"]))

    service.handleEvent(Event(EventType.DEPLOY_SUCCESS, "1.0.2", ["carol"]))
    assert service.deploys == []

    assert len(notification.messages) == 3
    authors = {m.author for m in notification.messages}
    assert authors == {"alice", "bob", "carol"}
    for m in notification.messages:
        assert m.version_no == "1.0.2"
        assert "success" in m.text
