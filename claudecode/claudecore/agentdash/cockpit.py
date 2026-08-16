from claudecore.event_bus import bus

class AgentDashCockpit:
    def __init__(self):
        self.events = {
            "stimulus": [],
            "spike": [],
            "anomaly": [],
            "defense": []
        }

    def record_event(self, event_type, payload):
        if event_type in self.events:
            self.events[event_type].append(payload)

    def render(self):
        print("\n=== AGENTDASH COCKPIT ===")

        print("\n-- Stimuli --")
        for s in self.events["stimulus"]:
            print(f"  {s}")

        print("\n-- Spikes --")
        for sp in self.events["spike"]:
            print(f"  Neuron {sp['neuron']} fired (energy={sp['energy']})")

        print("\n-- Anomalies --")
        for a in self.events["anomaly"]:
            print(f"  {a['path']} | score={a['score']}")

        print("\n-- Defense Actions --")
        for d in self.events["defense"]:
            print(f"  {d}")

        print("\n==========================\n")
