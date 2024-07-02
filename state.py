from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    El contexto define la interfaz de interés para los clientes. También mantiene una referencia 
    a una instancia de una subclase State, que representa el estado actual de Context.
    """
    _state = None
    """
    Una referencia al estado actual de Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        El contexto permite cambiar el objeto State en tiempo de ejecución.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    El Context delega parte de su comportamiento en el objeto State actual.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
     La clase State base declara los métodos que todos los Concrete State deben 
     implementar y también proporciona una referencia inversa al objeto Context, 
     asociado con el State. Esta referencia inversa puede ser utilizada por States
     para realizar la transición de Context a otro State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Los estados concretos implementan varios comportamientos, asociados con un estado del
Contexto.
"""


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # Codigo del cliente.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()