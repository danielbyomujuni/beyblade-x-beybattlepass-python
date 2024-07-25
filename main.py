import asyncio
import binascii
from bleak import BleakClient
import logging
import discover

logger = logging.getLogger(__name__)

device_address = "da:c4:51:02:25:b7"

def callback(sender, data):
    print(f"[{sender}]: {data}")

async def main():
    address = await discover.scan_battle_pass();

    if (address == None):
        return;

    async with BleakClient(address) as client:
        print("connected to battlepass")

        for service in client.services:
            print(f"[Service] {service}")
            for characteristics in service.characteristics:
                print(f"    [Characteristic] {characteristics}")


        #print(f"\n[Characteristic] {client.services.get_characteristic(15)}")
        #start notify
        await client.start_notify(17, callback)

        await client.write_gatt_char(client.services.get_characteristic(15).uuid, bytes.fromhex('51'));

        print("scanning")

        for i in range(0, 16 * 8):
            print(i)
            await client.write_gatt_char(client.services.get_characteristic(15).uuid, i.to_bytes());
            await asyncio.sleep(0.5)

        await client.stop_notify(client.services.get_characteristic(17))
        print("disconnected from battlepass")

asyncio.run(main())