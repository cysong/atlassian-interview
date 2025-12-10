
from typing import List


class Event:
    event_type: str  # DeployStart| DeploySucess | DeployFail
    authors: List[str]
    version_no: str

class Message:
    def __init__(self, author, version_no, text) -> None:
        self.author = author
        self.version_no = version_no
        self.text=text

class EventService:
    def __init__(self) -> None:
        self.deploys:List[Event] = []
        self.notification = NotificationService()

    def handleEvent(self, event: Event):
        if event is None:
            return
        if event.event_type =='DeployFail':
            self.deploys.append(event)
        elif event.event_type =='DeploySucess':
            authors = []
            for e in self.deploys:
                authors.append(e.authors)
            authors.append(event.authors)
            message = f'Deploy of version {event.version_no} is success!'
            for author in authors:
                self.notification.receiveMessage(Message(author, event.version_no, message))
            self.deploys=[]
        


class NotificationService:
    def __init__(self) -> None:
        self.messages = [] 

    def receiveMessage(self, message: Message):
        self.messages.append(message)
    def sendNotifications(self):
        pass