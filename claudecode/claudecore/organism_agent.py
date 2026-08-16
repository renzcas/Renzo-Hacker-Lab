from claudecore.agent_base import ClaudeAgent
from claudecore.event_bus import bus

class OrganismAgent(ClaudeAgent):
    def __init__(self):
        super().__init__("OrganismAgent")
        self.neurons = [
            {"id": 1, "energy": 0.2, "threshold": 0.5},
            {"id": 2, "energy": 0.1, "threshold": 0.4},
            {"id": 3, "energy": 0.3, "threshold": 0.6},
        ]

    def process_stimulus(self, stimulus):
        """
        Simple rule:
        - each stimulus increases neuron energy
        - if energy > threshold → emit spike event
        """
        intensity = stimulus.get("intensity", 0.1)

        for n in self.neurons:
            n["energy"] += intensity

            if n["energy"] > n["threshold"]:
                spike = {
                    "type": "spike",
                    "neuron": n["id"],
                    "energy": n["energy"]
                }
                bus.emit("spike", spike)

    def run(self):
        # Subscribe to CaveAgent stimulus
        self.on_event("stimulus", self.process_stimulus)
