from abc import ABC, abstractmethod

from core.actions import Action


class Driver(ABC):

    @abstractmethod
    def execute(self, action: Action) -> None:
        pass