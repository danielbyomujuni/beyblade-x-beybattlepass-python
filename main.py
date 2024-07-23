import asyncio
import binascii
from bleak import BleakClient


device_address = "da:c4:51:02:25:b7"
lock = 0;


def callback(sender, data):
    print(f"{sender}: {data}")
    lock = 1;

async def main(address):
    async with BleakClient(address) as client:
        print("connected")
        await client.start_notify("55c4f002-f8eb-11ec-b939-0242ac120002", callback)
        print("requesting data")
        await client.write_gatt_char("55c4f001-f8eb-11ec-b939-0242ac120002", bytes.fromhex('51'));
        await asyncio.sleep(5.0)
        await client.stop_notify("55c4f002-f8eb-11ec-b939-0242ac120002");
        print("done :)")
        


asyncio.run(main(device_addre