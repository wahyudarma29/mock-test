from itertools import cycle

from core.interfaces.proxy_manager import ProxyManager


class DummyProxyManager(ProxyManager):

    def __init__(self):
        self._proxies = cycle(
            [
                "proxy-1",
                "proxy-2",
                "proxy-3",
            ]
        )

        self.current_proxy = next(self._proxies)

    def rotate_proxy(self) -> str:
        self.current_proxy = next(self._proxies)

        print(
            f"[PROXY] Switched to {self.current_proxy}"
        )

        return self.current_proxy