#!/usr/bin/env python3

import asyncio
import websockets

TELEMETRY_URL = "ws://localhost:8765"

async def scan_telemetry():
    print("\n=== Renzo Hacker Lab — Telemetry Scanner ===")
    print(f"Connecting to {TELEMETRY_URL} ...")

    try:
        async with websockets.connect(TELEMETRY_URL) as ws:
            print("Connected. Listening for packets...\n")

            while True:
                packet = await ws.recv()
                print(f"[Telemetry] {packet}")

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(scan_telemetry())
