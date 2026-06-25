from abc import ABC, abstractmethod

from core.bridge import Bridge

class BaseAgent(ABC):
    def __init__(self, bridge: Bridge):
        self.bridge = bridge

    @abstractmethod
    def run(self) -> None:
        pass