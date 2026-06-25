from fastapi import APIRouter

from api.schemas import ActionRequest

from core.actions import Action
from core.bridge import Bridge

router = APIRouter()


def get_bridge() -> Bridge:
    from drivers.android_driver import (
        AndroidDriver,
    )

    from core.proxy.manager import (
        DummyProxyManager,
    )

    return Bridge(
        driver=AndroidDriver(),
        proxy_manager=DummyProxyManager(),
    )

@router.get("/")
def service_running():
    return {
        "message": "Service Running"
    }

@router.post("/actions")
def execute_action(
    payload: ActionRequest,
):

    bridge = get_bridge()

    bridge.execute(
        Action(payload.action)
    )

    return {
        "status": "success",
        "action": payload.action,
    }