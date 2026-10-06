#!/usr/bin/env python3

import random

def generate_heatmap(size=5):
    return [
        [random.randint(0, 100) for _ in range(size)]
        for _ in range(size)
    ]

def corruption_diagnostics(heatmap):
    flat = [v for row in heatmap for v in row]
    avg = sum(flat) / len(flat)
    peak = max(flat)

    if avg < 20:
        status = "Dormant corruption field"
    elif avg < 50:
        status = "Active corruption currents"
    elif avg < 80:
        status = "⚠ Corruption storm forming"
    else:
        status = "🌋 Cataclysmic corruption surge"

    return avg, peak, status

def scan_corruption():
    print("\n=== Renzo Hacker Lab — Corruption Scanner ===")

    heatmap = generate_heatmap()
    avg, peak, status = corruption_diagnostics(heatmap)

    print("\n-- Heatmap --")
    for row in heatmap:
        print(" ".join(f"{v:3d}" for v in row))

    print("\n-- Diagnostics --")
    print(f"Average Corruption: {avg:.2f}")
    print(f"Peak Corruption: {peak}")
    print(f"Status: {status}")

if __name__ == "__main__":
    scan_corruption()
