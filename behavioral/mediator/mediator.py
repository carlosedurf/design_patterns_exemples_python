from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Collegue(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass


class Person(Collegue):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, collegue: Collegue, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Collegue, receiver: str, msg: str) -> None:
        pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.collegues: List[Collegue] = []

    def is_collegue(self, collegue: Collegue) -> bool:
        return collegue in self.collegues

    def add(self, collegue: Collegue) -> None:
        if not self.is_collegue(collegue):
            self.collegues.append(collegue)

    def remove(self, collegue: Collegue) -> None:
        if self.is_collegue(collegue):
            self.collegues.remove(collegue)

    def broadcast(self, collegue: Collegue, msg: str) -> None:
        if not self.is_collegue(collegue):
            return

        print(f'{collegue.name} disse: {msg}')

    def direct(self, sender: Collegue, receiver: str, msg: str) -> None:
        if not self.is_collegue(sender):
            return

        receiver_obj: List[Collegue] = [
            collegue for collegue in self.collegues
            if collegue.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == "__main__":
    chat = Chatroom()

    joao = Person('João', chat)
    maria = Person('Maria', chat)
    elis = Person('Elis', chat)
    jose = Person('José', chat)

    chat.add(joao)
    chat.add(maria)
    chat.add(elis)
    chat.add(jose)

    joao.broadcast('Olá pessoas')
    maria.broadcast('Fala, beleza')
    jose.broadcast('Eu não fui adicionado ao chat')

    print()

    joao.send_direct('Maria', 'Oi Maria, tudo bem?')
    maria.send_direct('João', 'Bem e você?')