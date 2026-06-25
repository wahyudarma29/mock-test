from core.bridge import Bridge
from agents.tasks import (
    OPEN_APP,
    SCROLL,
    LIKE,
)

class SocialAgent:

    def __init__(self, bridge: Bridge):
        self.bridge = bridge

    def run(self):

        self.bridge.execute(OPEN_APP)
        self.bridge.execute(SCROLL)
        self.bridge.execute(LIKE)

        print("[AGENT] Task complete")