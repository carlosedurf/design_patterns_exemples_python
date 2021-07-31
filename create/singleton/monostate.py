class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class A(StringReprMixin):
    def __init__(self, name) -> None:
        self.x = 10
        self.y = 20
        self.name = name


class MonoState(StringReprMixin):
    _state: dict = {}
    x: int = 0

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None) -> None:
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class A2(MonoState):
    pass


if __name__ == "__main__":
    a = A("Carlos")
    print(a)
    print()

    m1 = MonoState(nome="Carlos")
    m2 = MonoState(sobrenome="Eduardo")
    a2 = A2()

    m1.x = 15
    print(m1)
    print(m2)
    print(a2)
