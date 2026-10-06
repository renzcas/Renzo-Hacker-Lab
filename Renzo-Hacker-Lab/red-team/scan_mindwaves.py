#!/usr/bin/env python3

from mindwaves import MindwaveCore

def scan_mindwaves():
    mw = MindwaveCore()

    print("\n=== Renzo Hacker Lab — Mindwave Scanner ===")

    print(f"Pulse Frequency: {mw.pulse_frequency} Hz")
    print(f"Coherence: {mw.coherence}")
    print(f"Harmonic Bands: {mw.harmonic_bands}")
    print(f"Resonance Level: {mw.resonance}")
    print(f"Corruption Echo: {mw.corruption_echo}")

    # Derived diagnostics
    if mw.coherence < 0.3:
        print("Status: ⚠ Chaotic mindwave field")
    elif mw.coherence < 0.7:
        print("Status: Stable but reactive")
    else:
        print("Status: ⚡ High‑coherence harmonic alignment")

if __name__ == "__main__":
    scan_mindwaves()
