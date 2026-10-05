# TODO: organ wheel rendering
def render_organ_wheel(state):
    """
    Simple text-based organ wheel.
    Later you can replace this with a radial graphic.
    """
    organs = [
        "nature", "truth", "memory", "balance",
        "swarm", "industrial", "corruption",
        "pattern", "binary", "techno", "decision"
    ]

    print("\n=== ORGAN WHEEL ===")
    for organ in organs:
        value = state.get(organ, 0.0)
        print(f"{organ.capitalize():12}: {value:.2f}")
