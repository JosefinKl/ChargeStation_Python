print("Hej laddvärlden 🚗⚡")

import charger


plug_connected = True

charge_start = input("Write 'Start' to start charging: ")

if charge_start == "Start":
    print("Charging started")
    charger.charging(0, True)


