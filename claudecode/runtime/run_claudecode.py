from claudecore.event_bus import bus
from claudecore.scanner import scan_repo
from claudecore.defender import defend
from claudecore.cave_agent import CaveAgent
from claudecore.organism_agent import OrganismAgent
from claudecore.binarycommand_agent import BinaryCommandAgent

from agentdash.cockpit import AgentDashCockpit
from agentdash.panels.event_panel import attach_cockpit

from ute.runtime.update_cycle import run_ute_cycle

def run_claudecode():
    cave = CaveAgent()
    organism = OrganismAgent()
    binary = BinaryCommandAgent()
    cockpit = AgentDashCockpit()

    attach_cockpit(cockpit)

    bus.subscribe("anomaly", defend)

    # 1. Run agents
    organism.run()
    stimulus = cave.run()

    # 2. Run scanner
    anomalies = scan_repo()
    for a in anomalies:
        bus.emit("anomaly", a)

    # 3. BinaryCommandAgent fuzz + defense
    fuzz_events, defense_signals = binary.run(anomalies)

    # 4. Run UTE
    ute_state = run_ute_cycle({
        "stimulus": stimulus,
        "spikes": cockpit.events["spike"],
        "anomalies": anomalies,
        "fuzz": fuzz_events,
        "defense": defense_signals
    })

    # 5. Render cockpit
    cockpit.render()

    print("UTE STATE:")
    print("Embeddings:", ute_state.embeddings)
    print("Vectors:", ute_state.vectors)
    print("Tensors:", ute_state.tensors)
    print("Physics:", ute_state.physics)

if __name__ == "__main__":
    run_claudecode()
