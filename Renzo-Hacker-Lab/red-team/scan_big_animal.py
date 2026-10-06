#!/usr/bin/env python3

from BigAnimalCore import BigAnimalCore
from BigAnimaState import BigAnimaState

def scan_big_animal():
    core = BigAnimalCore()
    state = BigAnimaState()

    print("\n=== Renzo Hacker Lab — Big Animal Scanner ===")

    # Core life-force variables
    print(f"Nature: {core.nature}")
    print(f"Truth: {core.truth}")
    print(f"Memory: {core.memory}")
    print(f"Balance: {core.balance}")

    # Entropy variables
    print(f"Swarm: {core.swarm}")
    print(f"Corruption: {core.corruption}")
    print(f"Industrial: {core.industrial}")
    print(f"Emotional Storm: {core.emotional_storm}")

    # Meta-stabilizers
    print(f"Pattern: {core.pattern}")
    print(f"Binary: {core.binary}")
    print(f"Techno: {core.techno}")

    # Global threats
    print(f"WW3 Escalation: {core.ww3_escalation}")

    # State machine
    print(f"Current State: {state.current_state}")
    print(f"State History: {state.history}")

if __name__ == "__main__":
    scan_big_animal()
