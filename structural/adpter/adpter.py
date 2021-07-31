from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass

class Control(IControl):
    def top(self) -> None:
        print('Movendo para cima...')

    def right(self) -> None:
        print('Movendo para direita...')

    def down(self) -> None:
        print('Movendo para baixo...')

    def left(self) -> None:
        print('Movendo para esquerda...')


class NewControl:
    def new_top(self) -> None:
        print('New Control: Movendo para cima...')

    def new_right(self) -> None:
        print('New Control: Movendo para direita...')

    def new_down(self) -> None:
        print('New Control: Movendo para baixo...')

    def new_left(self) -> None:
        print('New Control: Movendo para esquerda...')


class ControlAdapter:
    """ Adapter Object """

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.new_top()

    def right(self) -> None:
        self.new_control.new_right()

    def down(self) -> None:
        self.new_control.new_down()

    def left(self) -> None:
        self.new_control.new_left()


class ControlAdapter2(Control, NewControl):
    """ Adapter Class """

    def top(self) -> None:
        self.new_top()

    def right(self) -> None:
        self.new_right()

    def down(self) -> None:
        self.new_down()

    def left(self) -> None:
        self.new_left()

if __name__ == "__main__":

    # Control - Adapter object
    new_control = NewControl()
    control_object = ControlAdapter(new_control)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()

    # Control - Adapter class
    control_class = ControlAdapter2()
    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()

