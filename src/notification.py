
from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
from time import sleep
from typing import Deque, List

class EventType(Enum):
    DEPLOY_START = 'DeployStart'
    DEPLOY_FAIL = 'DeployFail'
    DEPLOY_SUCCESS = 'DeploySuccess'

class Event:
    def __init__(self, event_type: EventType, version_no: str, authors: List[str]) -> None:
        self.event_type = event_type
        self.version_no = version_no
        self.authors = authors

class Message:
    def __init__(self, author:str, version_no: str, text:str) -> None:
        self.author = author
        self.version_no = version_no
        self.text=text

class NotificationSender(ABC):
    @abstractmethod
    def send_message(self, message: Message) -> None:
        pass

class ConsoleNotification(NotificationSender):
    def __init__(self) -> None:
        self.messages: Deque[Message] = deque()

    def send_message(self, message: Message) -> None:
        self.messages.append(message)

    def process_next(self) -> bool:
        # Process the next message in the queue
        if not self.messages:
            return False
        message = self.messages.popleft()
        self._send(message)
        return True
    
    def _send(self, message: Message):
        print(f'Sending notification to {message.author}: {message.text}')

    def continue_processing(self):
        # Continuously process messages
        while True:
           processed = self.process_next()
           if not processed:
               sleep(1)


class EventService:
    def __init__(self, notification: NotificationSender) -> None:
        self.deploys:List[Event] = []
        self.notification = notification

    def handleEvent(self, event: Event):
        if event is None:
            return
        if event.event_type == EventType.DEPLOY_FAIL:
            self.deploys.append(event)
        elif event.event_type == EventType.DEPLOY_SUCCESS:
            authors = set()
            for e in self.deploys:
                authors.update(e.authors)
            self.deploys.clear()
            authors.update(event.authors)

            message = f'Deploy of version {event.version_no} is success!'
            for author in authors:
                self.notification.send_message(Message(author, event.version_no, message))
