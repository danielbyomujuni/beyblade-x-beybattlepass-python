import asyncio
import binascii
from bleak import BleakClient
import logging
import discover
import socket

logger = logging.getLogger(__name__)

device_address = "da:c4:51:02:25:b7"

def callback(sender, data):
    print(f"[{sender}]: {binascii.hexlify(data)}")

async def main():
    address = await discover.scan_battle_pass();

    if (address == None):
        return;

    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM);
    client.connect((address, 4))
    print("connected to battlepass")
    try:
        while True:
            message = bytes.fromhex('0240000900050004001213000100')
            client.send(message);
            data = client.recv(1024)
    except:
        print("error")




    print("disconnected from battlepass")

asyncio.run(main())