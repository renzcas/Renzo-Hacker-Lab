class AgentManager:
    """
    Holds all agents and updates them each tick.
    """

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def update(self, state, events, dt: float):
        for agent in self.agents:
            agent.update(state, events, dt)
