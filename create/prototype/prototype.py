from __future__ import annotations

from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addressess: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addressess.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":

    carlos = Person("Carlos", "Rocha")
    address_carlos = Address("Av Comendador Teles", "2475")
    carlos.add_address(address_carlos)

    esposa_carlos = carlos.clone()
    esposa_carlos.firstname = "Glauce"

    print(carlos)
    print(esposa_carlos)
