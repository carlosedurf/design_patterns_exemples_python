from abc import ABC, abstractmethod


class LuxuryVehicle(ABC):
    def search_customer(self) -> None:
        pass


class PopularVehicle(ABC):
    def search_customer(self) -> None:
        pass


class LuxuryCarNZ(LuxuryVehicle):
    def search_customer(self) -> None:
        print("Luxury car NZ is looking for a customer...")


class PopularCarNZ(PopularVehicle):
    def search_customer(self) -> None:
        print("Popular car NZ is looking for a customer...")


class LuxuryMotocycleNZ(LuxuryVehicle):
    def search_customer(self) -> None:
        print("Luxury motorcycle NZ is looking for a customer...")


class PopularMotocycleNZ(PopularVehicle):
    def search_customer(self) -> None:
        print("Popular motorcycle NZ is looking for customer...")


class LuxuryCarSZ(LuxuryVehicle):
    def search_customer(self) -> None:
        print("Luxury car SZ is looking for a customer...")


class PopularCarSZ(PopularVehicle):
    def search_customer(self) -> None:
        print("Popular car SZ is looking for a customer...")


class LuxuryMotocycleSZ(LuxuryVehicle):
    def search_customer(self) -> None:
        print("Luxury motorcycle SZ is looking for a customer...")


class PopularMotocycleSZ(PopularVehicle):
    def search_customer(self) -> None:
        print("Popular motorcycle SZ is looking for customer...")


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_car() -> PopularVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_luxury_motocycle() -> LuxuryVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_motocycle() -> PopularVehicle:
        pass


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarNZ()

    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarNZ()

    @staticmethod
    def get_luxury_motocycle() -> LuxuryVehicle:
        return LuxuryMotocycleNZ()

    @staticmethod
    def get_popular_motocycle() -> PopularVehicle:
        return PopularMotocycleNZ()


class SouthZoneVeiculoFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarSZ()

    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarSZ()

    @staticmethod
    def get_luxury_motocycle() -> LuxuryVehicle:
        return LuxuryMotocycleSZ()

    @staticmethod
    def get_popular_motocycle() -> PopularVehicle:
        return PopularMotocycleSZ()


class Client:
    def search_customer(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVeiculoFactory()]:
            popular_car = factory.get_popular_car()
            popular_car.search_customer()

            luxury_car = factory.get_luxury_car()
            luxury_car.search_customer()

            popular_motocycle = factory.get_popular_motocycle()
            popular_motocycle.search_customer()

            luxury_motocycle = factory.get_luxury_motocycle()
            luxury_motocycle.search_customer()


if __name__ == "__main__":
    client = Client()
    client.search_customer()
