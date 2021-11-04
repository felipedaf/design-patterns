"""
Mediator Design Pattern

Motivation:
 - Components may go in and out of a system at any time

 - It makes no sense for them to have direct references to one another

 Solution: have them all refer to some central component that facilitates communication
"""

class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self) -> None:
        self.people = []


    def join(self, person):
        join_msg = f'{person.name} joints the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)


    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)


    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)

if __name__ == '__main__':
    room = ChatRoom()

    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say('hi room!')
    jane.say('oh, hey john')

    simon = Person('Simon')
    room.join(simon)
    simon.say('hi everyone!')

    jane.private_message()