from agents.agents import SocialAgent


class Crew:

    def __init__(self, agent: SocialAgent):
        self.agent = agent

    def kickoff(self):
        self.agent.run()