from __future__ import annotations

from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    """ Subject Interface """

    firstname: str
    lastname: str

    @abstractmethod
    def get_address(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class RealUser(IUser):
    """ Real Subject """
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)    # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_address(self) -> List[Dict]:
        sleep(2)    # Simulando requisição
        return [
            {'rua': 'Av. Presidente Vargas', 'numero': 700}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)    # Simulando requisição
        return {
            'cpf': '111.111.111-11',
            'rg': '11.111.111-1'
        }


class UserProxy(IUser):
    """ Proxy """
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        self._cache_addressess: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_address(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cache_addressess'):
            self._cache_addressess = self._real_user.get_address()

        return self._cache_addressess

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    user = UserProxy('Carlos', 'Eduardo')

    print(user.firstname)
    print(user.lastname)

    # 6 segundos
    print(user.get_all_user_data())
    print(user.get_address())

    print("CACHED DATA:")

    # Responde instantâneamente, pegando do cache
    for i in range(50):
        print(user.get_address())
