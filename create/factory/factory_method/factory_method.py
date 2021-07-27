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


class VehicleFactory(ABC):
    def __init__(self, tipo: str) -> None:
        self.carro: Vehicle = self.get_car(tipo)

    @staticmethod
    @abstractmethod
    def get_car(tipo: str) -> Vehicle:
        pass

    def search_customer(self) -> None:
        self.carro.search_customer()


class NorthZoneVehicleFactory(VehicleFactory):
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


class ZonaSulVeiculoFactory(VehicleFactory):
    @staticmethod
    def get_car(tipo: str) -> Vehicle:
        if tipo == "popular":
            return PopularCar()

        assert 0, "Vehicle not exists"


if __name__ == "__main__":
    from random import choice

    availables_vehicles_north_zone = [
        "luxury",
        "popular",
        "motocycle",
        "luxury_motocycle",
    ]
    availables_vehicles_south_zone = ["popular"]

    print("-------------------------------------------")
    print("##### NORTH ZONE #####")
    print("-------------------------------------------")
    for i in range(10):
        car = NorthZoneVehicleFactory(choice(availables_vehicles_north_zone))
        car.search_customer()

    print()
    print()

    print("-------------------------------------------")
    print("##### SOUTH ZONE #####")
    print("-------------------------------------------")
    for i in range(10):
        car2 = ZonaSulVeiculoFactory(choice(availables_vehicles_south_zone))
        car2.search_customer()
