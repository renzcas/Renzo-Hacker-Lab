from organism.world_organism import WorldOrganism

class CLICommands:
    """
    Command-line interface for controlling the BIG ANIMAL.
    """

    def __init__(self):
        self.world = WorldOrganism()

    def cmd_run(self, ticks=50, dt=1.0):
        """
        Run the simulation for a number of ticks.
        """
        print(f"\n[RUN] Starting simulation for {ticks} ticks...\n")
        for i in range(ticks):
            print(f"\n--- TICK {i+1} ---")
            self.world.step(dt)

    def cmd_save(self, path="world_state.json"):
        """
        Save the current world state.
        """
        self.world.save_state(path)

    def cmd_load(self, path="world_state.json"):
        """
        Load a world state.
        """
        self.world.load_state(path)

    def cmd_pulse(self):
        """
        Print the current worldheart pulse.
        """
        pulse = self.world.state["pulse"]
        print(f"\n[PULSE] Current pulse: {pulse:.2f}")

    def cmd_organs(self):
        """
        Print all organ values.
        """
        print("\n[ORGANS]")
        for k, v in self.world.state.items():
            if isinstance(v, (int, float)):
                print(f"{k:12}: {v:.2f}")

    def cmd_ascend(self):
        """
        Force ascension.
        """
        print("\n[ASCEND] Forcing ascension...")
        self.world.state["pulse"] = 5.0
        self.world.state["truth"] = 3.0
        self.world.endgame.update(self.world.state, [], 1.0)

    def cmd_collapse(self):
        """
        Force collapse.
        """
        print("\n[COLLAPSE] Forcing collapse...")
        self.world.state["pulse"] = -5.0
        self.world.state["corruption"] = 4.0
        self.world.state["ww3_escalation"] = 3.0
        self.world.endgame.update(self.world.state, [], 1.0)
