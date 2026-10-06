#!/usr/bin/env python3
import random
import time

def world_scan():
    creatures = random.randint(1, 50)
    corruption = random.randint(0, 100)
    anomaly = random.choice(["None", "Minor Rift", "Major Rift", "Cataclysm"])

    print("\n=== Renzo Hacker Lab — World Scan ===")
    print(f"Creatures detected: {creatures}")
    print(f"Corruption level: {corruption}")
    print(f"Anomaly signature: {anomaly}")

if __name__ == "__main__":
    while True:
        world_scan()
        time.sleep(1)
