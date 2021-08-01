from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    # Leaf
    camiseta1 = Product("Camiseta 1", 10)
    camiseta2 = Product("Camiseta 2", 10)
    camiseta3 = Product("Camiseta 3", 10)
    camiseta3.print_content()

    # Composite
    caixa_camisetas = Box("Caixa de Camiseta")
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)
    caixa_camisetas.print_content()

    # Leaf
    smartphone1 = Product('iPhone', 10000)
    smartphone2 = Product('Samsung Note', 10000)

    print()

    # Composite
    caixa_smartphones = Box("Caixa de Smartphone")
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)
    caixa_smartphones.print_content()

    print()

    # Composite
    caixa_grande = Box("Caixa Grande")
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())
