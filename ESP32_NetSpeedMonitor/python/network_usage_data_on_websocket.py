import psutil
import time
import asyncio
import websockets

UPDATE_DELAY = 0.2  # in seconds
WEBSOCKET_SERVER = "ws://192.168.0.103:80/ws"

async def send_data(websocket, data):
    await websocket.send(data)

def get_size(bits):
    """
    Returns size of bits in megabits
    """
    return f"{bits / (1024 * 1024):.2f}Mb"


async def get_network_stats(websocket):
    bytes_sent, bytes_recv = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv

    while True:
        await asyncio.sleep(UPDATE_DELAY)  # Replace time.sleep() with asyncio.sleep()
        io = psutil.net_io_counters()
        us, ds = io.bytes_sent - bytes_sent, io.bytes_recv - bytes_recv
        us_bits, ds_bits = us * 8, ds * 8
        upload_speed = us_bits / UPDATE_DELAY
        download_speed = ds_bits / UPDATE_DELAY
        total_sent = io.bytes_sent
        total_received = io.bytes_recv
        current_sent = us
        current_received = ds

        # Format the data
        data = f"us: {get_size(upload_speed)}; ds: {get_size(download_speed)}"

        # Print data to CLI
        print(f"Upload: {get_size(total_sent)}   "
              f", Download: {get_size(total_received)}   "
              f", Upload Speed: {get_size(upload_speed)}/s   "
              f", Download Speed: {get_size(download_speed)}/s      ", end="\r")

        # Send data via WebSocket
        await send_data(websocket, data)

        # Update bytes_sent and bytes_recv for next iteration
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

async def main():
    async with websockets.connect(WEBSOCKET_SERVER) as websocket:
        await get_network_stats(websocket)

if __name__ == "__main__":
    asyncio.run(main())
