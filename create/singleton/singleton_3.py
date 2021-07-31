from typing import Dict


class Meta(type):
    def __call__(cls, *args, **kwargs) -> None:
        print("CALL é executado")
        super().__call__(*args, **kwargs)


class Peaple(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("New é executado")
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        print("INIT é executado")
        self.name = name

    def __call__(self, x, y):
        print("call chamando ", self.name, x + y)


p1 = Peaple("Carlos")
print(p1.name)


###########################################################################


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        """O Init será chamado todas as vezes"""
        self.tema = "Tema escuro"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "Tema claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
