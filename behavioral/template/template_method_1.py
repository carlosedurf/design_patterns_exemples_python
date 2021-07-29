from abc import ABC, abstractmethod

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self):
        pass

    def base_class_method(self) -> None:
        print('Sendo executado também')

    @abstractmethod
    def operation1(self) -> None:
        pass

    @abstractmethod
    def operation2(self) -> None:
        pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Utilizando o HOOK')

    def operation1(self) -> None:
        print('Operação 1 concluída')

    def operation2(self) -> None:
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self) -> None:
        print('Operação 1 concluída (diferente)')

    def operation2(self) -> None:
        print('Operação 2 concluída (diferente)')

if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()