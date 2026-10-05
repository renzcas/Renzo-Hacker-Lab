import time
from organism.world_organism import WorldOrganism

def run(tick_rate=0.5, max_ticks=None):
    """
    Runs the BIG ANIMAL simulation.
    
    tick_rate: seconds between ticks
    max_ticks: optional limit for number of ticks (None = infinite)
    """

    world = WorldOrganism()
    tick = 0

    print("\n=== BIG ANIMAL SIMULATION START ===\n")

    while True:
        # Tick counter
        tick += 1
        print(f"\n--- TICK {tick} ---")

        # Step the organism
        state, events = world.step(dt=1.0)

        # Optional tick limit
        if max_ticks is not None and tick >= max_ticks:
            print("\n=== SIMULATION COMPLETE ===")
            break

        # Wait for next tick
        time.sleep(tick_rate)
