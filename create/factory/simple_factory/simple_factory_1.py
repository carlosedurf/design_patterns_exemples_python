from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def search_customer(self) -> None:
        pass


class LuxuryCar(Vehicle):
    def search_customer(self) -> None:
        print("Luxury car is looking for a customer...")


class PopularCar(Vehicle):
    def search_customer(self) -> None:
        print("Popular car is looking for a customer...")


class LuxuryMotocycle(Vehicle):
    def search_customer(self) -> None:
        print("Luxury motorcycle is looking for a customer...")


class PopularMotocycle(Vehicle):
    def search_customer(self) -> None:
        print("Popular motorcycle is looking for customer...")


class VehicleFactory:
    def __init__(self, type: str) -> None:
        self.carro: Vehicle = self.get_car(type)

    @staticmethod
    def get_car(type: str) -> Vehicle:
        if type == "luxury":
            return LuxuryCar()

        if type == "popular":
            return PopularCar()

        if type == "luxury_motocycle":
            return LuxuryMotocycle()

        if type == "motocycle":
            return PopularMotocycle()

        assert 0, "Vehicle not exists"

    def search_customer(self) -> None:
        self.carro.search_customer()


if __name__ == "__main__":
    from random import choice

    available_cars = ["luxury", "popular", "motocycle", "luxury_motocycle"]

    for i in range(10):
        car = VehicleFactory.get_car(choice(available_cars))
        car.search_customer()

    print("-------------------------------------------------------")

    for i in range(10):
        car2 = VehicleFactory(choice(available_cars))
        car2.search_customer()
