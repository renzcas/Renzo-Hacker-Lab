#!/usr/bin/env python3

import asyncio
import websockets

PORT = 8765

async def handler(ws):
    print("Client connected")

    while True:
        await ws.send("CREATURES:17")
        await ws.send("CTA:Active")
        await ws.send("HEATMAP:1,2,3;4,5,6;7,8,9")
        await asyncio.sleep(1)

async def main():
    print(f"Telemetry server running on ws://0.0.0.0:{PORT}")
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
