# dispatcher.py

from organism.organs.commander.commander_core import Commander
from organism.organs.reality_mapper.mapper_core import RealityMapper

class Dispatcher:
    def __init__(self, state_store):
        self.commander = Commander(state_store)
        self.reality_mapper = RealityMapper(state_store)

    def tick(self, cognitive_inputs):
        # 1. Reality Mapper refines cognition
        refinement = self.reality_mapper.step(cognitive_inputs)

        # 2. Inject refinement into Commander inputs
        cognitive_inputs["refinement"] = refinement

        # 3. Commander issues swarm-level commands
        return self.commander.step(cognitive_inputs)
