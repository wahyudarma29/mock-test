import time

from core.actions import Action
from core.exceptions import (
    ProxyBannedError,
    DeviceDisconnectedError,
    AgentTaskAborted,
)
from core.interfaces.driver import Driver
from core.interfaces.proxy_manager import ProxyManager


class Bridge:

    MAX_RETRIES = 3

    def __init__(
        self,
        driver: Driver,
        proxy_manager: ProxyManager,
    ):
        self.driver = driver
        self.proxy_manager = proxy_manager

    def execute(self, action: Action) -> None:

        device_retry = 0

        while True:

            try:
                self.driver.execute(action)
                return

            except ProxyBannedError:

                print(
                    f"[BRIDGE] Proxy banned while "
                    f"executing {action.name}"
                )

                self.proxy_manager.rotate_proxy()

                print(
                    "[BRIDGE] Retrying same action..."
                )

                continue

            except DeviceDisconnectedError:

                device_retry += 1

                if device_retry > self.MAX_RETRIES:

                    raise AgentTaskAborted(
                        f"Device unavailable. "
                        f"Task aborted on action "
                        f"{action.name}"
                    )

                backoff = 2 ** (device_retry - 1)

                print(
                    f"[BRIDGE] Device disconnected. "
                    f"Retry {device_retry}/3 "
                    f"in {backoff}s"
                )

                time.sleep(backoff)