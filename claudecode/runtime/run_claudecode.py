from claudecore.event_bus import bus
from claudecore.scanner import scan_repo
from claudecore.defender import defend
from claudecore.cave_agent import CaveAgent
from claudecore.organism_agent import OrganismAgent

from agentdash.cockpit import AgentDashCockpit
from agentdash.panels.event_panel import attach_cockpit

from ute.runtime.update_cycle import run_ute_cycle

def run_claudecode():
    cave = CaveAgent()
    organism = OrganismAgent()
    cockpit = AgentDashCockpit()

    attach_cockpit(cockpit)

    bus.subscribe("anomaly", defend)

    # Collect events
    organism.run()
    stimulus = cave.run()

    anomalies = scan_repo()
    for a in anomalies:
        bus.emit("anomaly", a)

    # Gather spike events from cockpit
    spikes = cockpit.events["spike"]

    # Run UTE
    ute_state = run_ute_cycle({
        "stimulus": stimulus,
        "spikes": spikes,
        "anomalies": anomalies,
        "defense": cockpit.events["defense"]
    })

    cockpit.render()

    print("UTE STATE:")
    print("Embeddings:", ute_state.embeddings)
    print("Vectors:", ute_state.vectors)
    print("Tensors:", ute_state.tensors)
    print("Physics:", ute_state.physics)

if __name__ == "__main__":
    run_claudecode()
