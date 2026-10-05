# TODO: climate strip rendering
def render_climate_strip(state):
    """
    Shows a simple climate summary based on organ values.
    """
    swarm = state["swarm"]
    corruption = state["corruption"]
    industrial = state["industrial"]
    decision = state["decision"]

    print("\n=== CLIMATE STRIP ===")

    if swarm > 2.0:
        print("Swarm humidity rising...")
    if corruption > 2.0:
        print("Corruption fog thickening...")
    if industrial > 2.0:
        print("Industrial smog increasing...")
    if decision > 2.0:
        print("Emotional storms forming...")

    if swarm < 1.0 and corruption < 1.0 and industrial < 1.0:
        print("Calm zone detected.")
