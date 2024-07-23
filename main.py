import asyncio
import binascii
from bleak import BleakClient


device_address = "da:c4:51:02:25:b7"
async def main(address):
    print("awaiting battlepass")
    async with BleakClient(address) as client:
        print("connected to battlepass")


        print(client.services)


        print("disconnected from battlepass")
        #await client.write_gatt_char("2800", bytes.fromhex('51'));











        #print("connected")
        #await client.start_notify("55c4f002-f8eb-11ec-b939-0242ac120002", callback)
        #print("requesting data")
        #await client.write_gatt_char("55c4f001-f8eb-11ec-b939-0242ac120002", bytes.fromhex('51'));
        #await asyncio.sleep(5.0)
        #await client.stop_notify("55c4f002-f8eb-11ec-b939-0242ac120002");

        


asyncio.run(main(device_address))