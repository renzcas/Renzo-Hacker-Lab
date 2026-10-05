from big_animal.BigAnimalCore import BigAnimalCore
from big_animal.mindwaves import MindWaves
from big_animal.cave_bridge import CaveBridge

class BigAnimalKernel:
    def __init__(self):
        self.core = BigAnimalCore()
        self.mind = MindWaves()
        self.cave = CaveBridge()

    def tick(self, snapshot):
        # World simulation
        self.core.pre_tick(snapshot)
        self.core.tick(snapshot)
        self.core.post_tick(snapshot)

        # Snapshot after world update
        snap = self.core.snapshot()

        # Cognitive simulation
        self.mind.process(snap)

        # Feedback loop (optional)
        if hasattr(self.core, "apply_mindwaves"):
            self.core.apply_mindwaves(self.mind.output)

        # --- Cave Interface ---
        # Send MindWaves pulses to cave
        self.cave.send("mindwave", self.mind.output)

        # Send era changes
        self.cave.send("era", {"era": snap["era"]})

        # Send tribe updates
        self.cave.send("tribes", snap["tribes"])

        # Return combined state
        return {
            "world": snap,
            "mind": self.mind.output
        }
