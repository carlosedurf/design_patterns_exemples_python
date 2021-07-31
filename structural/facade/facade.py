from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class IObservable(ABC):
    """Observable"""

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherStation(IObservable):
    """Observable"""

    def __init__(self) -> None:
        self._oberservers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._oberservers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._oberservers:
            self._oberservers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._oberservers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Smarthphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f"{self.name} o objeto {observable_name} acabou de ser "
            f"atualizado => {self.observable.state}"
        )


class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self):
        state = self.observable.state
        print("Sou note e vou fazer outra coisa com esses dados.", state)

    def update(self) -> None:
        self.show()


class WheatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()

        self.smarthphone = Smarthphone("iPhone", self.weather_station)
        self.samsung = Smarthphone("Samsung", self.weather_station)
        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.smarthphone)
        self.weather_station.add_observer(self.samsung)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, oberserver: IObserver) -> None:
        self.weather_station.add_observer(oberserver)

    def remove_observer(self, oberserver: IObserver) -> None:
        self.weather_station.remove_observer(oberserver)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.samsung)

    def reset_state(self):
        self.weather_station.reset_state()

if __name__ == "__main__":
    weather_station = WheatherStationFacade()

    weather_station.change_state({"temperature": "30"})
    print()
    weather_station.change_state({"temperature": "32"})
    print()
    weather_station.change_state({"humidity": "63"})
    print()

    weather_station.remove_smartphone()
    weather_station.reset_state()
