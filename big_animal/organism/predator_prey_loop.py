def organism_step(state, dt: float):
    # Predator groups
    swarm = state["swarm"]
    corruption = state["corruption"]
    industrial = state["industrial"]

    # Prey groups
    nature = state["nature"]
    truth = state["truth"]
    memory = state["memory"]
    balance = state["balance"]

    # Modifiers / organs
    pattern = state["pattern"]      # vision cortex
    binary = state["binary"]        # bones / order
    techno = state["techno"]        # nerves / surveillance
    decision = state["decision"]    # prefrontal / emotional storms

    # --- Predator growth from prey consumption ---
    predator_pressure = nature + truth + memory + balance

    swarm += dt * (0.12 * predator_pressure - 0.05 * pattern)
    corruption += dt * (0.10 * predator_pressure - 0.04 * truth)
    industrial += dt * (0.08 * predator_pressure + 0.03 * techno)

    # --- Prey decline from predators ---
    predator_total = swarm + corruption + industrial

    nature -= dt * (0.10 * predator_total - 0.05 * balance)
    truth -= dt * (0.08 * predator_total - 0.06 * binary)
    memory -= dt * (0.06 * predator_total - 0.04 * truth)
    balance -= dt * (0.05 * predator_total - 0.07 * decision)

    # --- Pattern Seekers: reveal predators, reduce efficiency ---
    swarm *= (1 - 0.02 * pattern)
    corruption *= (1 - 0.015 * pattern)

    # --- Truth Judges: purify corruption, boost truth ---
    truth += dt * (0.04 * binary)

    # --- Decision Strategists: destabilize nature and balance ---
    nature -= dt * (0.03 * decision)
    balance -= dt * (0.02 * decision)

    # --- Industrial Iron: increases corruption baseline ---
    corruption += dt * 0.03

    # --- Clamp values to non-negative ---
    state["swarm"] = max(0.0, swarm)
    state["corruption"] = max(0.0, corruption)
    state["industrial"] = max(0.0, industrial)

    state["nature"] = max(0.0, nature)
    state["truth"] = max(0.0, truth)
    state["memory"] = max(0.0, memory)
    state["balance"] = max(0.0, balance)

    return state
next