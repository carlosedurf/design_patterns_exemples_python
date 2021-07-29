from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredientes() # Hook
        self.add_ingrentients() # Abstract
        self.hook_after_add_ingredientes() # Hook
        self.cook()             # Abstract
        self.cut()              # Concreto
        self.serve()            # Concreto

    def hook_before_add_ingredientes(self) -> None:
        pass

    def hook_after_add_ingredientes(self) -> None:
        pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza.')

    @abstractmethod
    def add_ingrentients(self) -> None:
        pass

    @abstractmethod
    def cook(self) -> None:
        pass


class AModa(Pizza):
    def add_ingrentients(self) -> None:
        print(f'AModa - Adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None:
        print(f'AModa - Cozinhando por 45min no forno a lenha')


class Veg(Pizza):
    def hook_before_add_ingredientes(self) -> None:
        print('Veg - Lavando ingredientes')

    def add_ingrentients(self) -> None:
        print(f'Veg - Adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        print(f'Veg - Cozinhando por 5min no forno comum')


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()