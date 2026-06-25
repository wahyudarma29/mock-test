from core.agents import BaseAgent
from agents.tasks import (
    OPEN_APP,
    SCROLL,
    LIKE,
)

class SocialAgent(BaseAgent):

    def run(self):
        self.bridge.execute(OPEN_APP)
        self.bridge.execute(SCROLL)
        self.bridge.execute(LIKE)
        print("[AGENT] workflow completed")