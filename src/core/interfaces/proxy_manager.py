from abc import ABC, abstractmethod


class ProxyManager(ABC):

    @abstractmethod
    def rotate_proxy(self) -> str:
        pass