from __future__ import annotations

from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount) -> None:
        self.discount: float = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == "__main__":
    twenty_percenty = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order = Order(1000, twenty_percenty)
    order2 = Order(1000, fifty_percent)
    order3 = Order(1000, no_discount)
    order4 = Order(1000, five_percent)

    print(order._total, order.total_with_discount)
    print(order2._total, order2.total_with_discount)
    print(order3._total, order3.total_with_discount)
    print(order4._total, order4.total_with_discount)
