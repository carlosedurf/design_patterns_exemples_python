from __future__ import annotations

from typing import Dict, List


class Client:
    """ Context """
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrisinc address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """ Flyweight """
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_detail: str) -> None:
        print(self._street, address_number, self._neighborhood, address_detail, self._zip_code)


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight: Address = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(street='Av Presidente Vargas', neighborhood='Centro', zip_code='12345-678')
    a2 = address_factory.get_address(street='Av Presidente Vargas', neighborhood='Centro', zip_code='12345-678')

    client1 = Client('Carlos')
    client1.address_number = '13'
    client1.address_details = 'APT'
    client1.add_address(a1)
    client1.list_addresses()

    client2 = Client('Glauce')
    client2.address_number = '453'
    client2.address_details = 'Casa'
    client2.add_address(a2)
    client2.list_addresses()
