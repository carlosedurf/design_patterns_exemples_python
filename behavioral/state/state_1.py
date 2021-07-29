from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
    """ Context """
    
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self) -> None:
        self.state.approve()

    def reject(self) -> None:
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente, não posso fazer nada.')

    def approve(self) -> None:
        self.order.state = PaymentApprove(self.order)
        print('Pagamento Aprovado')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento Recusado')


class PaymentApprove(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento Pendente')

    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada.')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento Recusado')


class PaymentReject(OrderState):
    def pending(self) -> None:
        print('Pagamento já recusado, não vou mover para pendente.')

    def approve(self) -> None:
        print('Pagamento já recusado, não vou posso aprovar.')

    def reject(self) -> None:
        print('Pagamento já recusado, não recusar novamente.')

if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
