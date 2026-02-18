print("Hej laddvärlden 🚗⚡")

import charger


plug_connected = True
charge_level = int (input("Write current charging level: "))
charge_start = input("Write 'Plug in' when plugged in: ")

charge_need = charger.batteryCapacity - charge_level*charger.batteryCapacity/100
time_to_charge = charge_need/charger.charger_power

print(time_to_charge)

if charge_start == "Plug in":
    print("Charger plugged in")
    charger.charging(charge_level, True)


