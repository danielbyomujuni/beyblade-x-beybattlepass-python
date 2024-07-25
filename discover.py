import asyncio

from bleak import BleakScanner


async def main():
    battlepass_address = await scan_battle_pass();
    print(battlepass_address);


async def scan_battle_pass(): 
    print("scanning for BeybattlePass for 5 seconds, please wait...")
    devices = await BleakScanner.discover(
        return_adv=True
    )

    for d, a in devices.values():
        if (a.local_name == "BEYBLADE_TOOL01"):
            print("Found BeybattlePass")
            return d.address

    print("Unable to find BeybattlePass")
    return None



if __name__ == "__main__":
    asyncio.run(main())