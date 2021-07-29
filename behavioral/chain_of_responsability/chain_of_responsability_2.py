from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{__class__.__name__}: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{__class__.__name__}: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerUnsolver(Handler):
    def handle(self, letter: str) -> str:
        return f'{__class__.__name__}: não tratou {letter}'

if __name__ == "__main__":
    handler_unsolver = HandlerUnsolver()
    handler_def = HandlerDEF(handler_unsolver)
    handle_abc = HandlerABC(handler_def)

    print( handle_abc.handle('A') )
    print( handle_abc.handle('B') )
    print( handle_abc.handle('C') )
    print( handle_abc.handle('D') )
    print( handle_abc.handle('E') )
    print( handle_abc.handle('F') )
    print( handle_abc.handle('G') )
    print( handle_abc.handle('H') )
    print( handle_abc.handle('I') )

    print()

    print( handler_def.handle('A') )
    print( handler_def.handle('B') )
    print( handler_def.handle('C') )
    print( handler_def.handle('D') )
    print( handler_def.handle('E') )
    print( handler_def.handle('F') )
    print( handler_def.handle('G') )
    print( handler_def.handle('H') )
    print( handler_def.handle('I') )

    print()

    print( handler_unsolver.handle('A') )
    print( handler_unsolver.handle('B') )
    print( handler_unsolver.handle('C') )
    print( handler_unsolver.handle('D') )
    print( handler_unsolver.handle('E') )
    print( handler_unsolver.handle('F') )
    print( handler_unsolver.handle('G') )
    print( handler_unsolver.handle('H') )
    print( handler_unsolver.handle('I') )
