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


        #await client.write_gatt_char(client.services.get_characteristic(15).uuid, bytes.fromhex('{:02X}'.format(81)));
        #await asyncio.sleep()

        # 01010001
        #print(binascii.hexlify(bytearray([0x51])))
        #await client.write_gatt_char(client.services.get_characteristic(15).uuid, bytearray([0x51]));
        print("scanning")

        #51
        for cmd in [81,116,117,97]:
            print('{:02X}: {}'.format(cmd, cmd))
            await client.write_gatt_char(client.services.get_characteristic(15).uuid, bytes.fromhex('{:02X}'.format(cmd)));
            await asyncio.sleep(5)

        #for i in range(70, 100):
        #    print('{:02X}: {}'.format(i, i))
        #    await client.write_gatt_char(client.services.get_characteristic(15).uuid, bytes.fromhex('{:02X}'.format(i)));
        #    await asyncio.sleep(1)

        await client.stop_notify(client.services.get_characteristic(17))
        print("disconnected from battlepass")

asyncio.run(main())