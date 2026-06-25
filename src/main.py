import logging
import sys
from agents.agents import SocialAgent
from agents.crew import Crew

from core.bridge import Bridge

from core.proxy.manager import (
    DummyProxyManager,
)

from drivers.android_driver import (
    AndroidDriver,
)

from core.exceptions import (
    AgentTaskAborted,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
)

def main():

    driver = AndroidDriver()

    proxy_manager = DummyProxyManager()

    bridge = Bridge(
        driver=driver,
        proxy_manager=proxy_manager,
    )

    agent = SocialAgent(bridge)

    crew = Crew(agent)

    try:
        crew.kickoff()

    except AgentTaskAborted as e:
        print(f"[SYSTEM] {e}")


if __name__ == "__main__":
    main()