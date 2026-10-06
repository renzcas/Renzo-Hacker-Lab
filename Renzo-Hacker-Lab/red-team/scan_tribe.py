#!/usr/bin/env python3

from TribeTech import TribeTech
from TribeRituals import TribeRituals
from TribeCorruption import TribeCorruption

def scan_tribe():
    tech = TribeTech()
    rituals = TribeRituals()
    corruption = TribeCorruption()

    print("\n=== Renzo Hacker Lab — Tribe Scanner ===")

    # Tribe Tech Diagnostics
    print("\n-- Tribe Technology --")
    print(f"Tech Level: {tech.level}")
    print(f"Artifacts: {tech.artifacts}")
    print(f"Upgrades: {tech.upgrades}")

    # Tribe Ritual Diagnostics
    print("\n-- Tribe Rituals --")
    print(f"Active Ritual: {rituals.active_ritual}")
    print(f"Ritual Power: {rituals.power}")
    print(f"Ritual Effects: {rituals.effects}")

    # Tribe Corruption Diagnostics
    print("\n-- Tribe Corruption --")
    print(f"Corruption Level: {corruption.level}")
    print(f"Corruption Pressure: {corruption.pressure}")
    print(f"Corruption Events: {corruption.events}")

if __name__ == "__main__":
    scan_tribe()
