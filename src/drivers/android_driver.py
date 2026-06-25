import random

from core.actions import Action
from core.exceptions import (
    ProxyBannedError,
    DeviceDisconnectedError,
)
from core.interfaces.driver import Driver


class AndroidDriver(Driver):

    def execute(self, action: Action) -> None:

        chance = random.random()

        if chance < 0.15:
            raise ProxyBannedError()

        if chance < 0.30:
            raise DeviceDisconnectedError()

        print(
            f"[ANDROID] Executed: {action.name}"
        )