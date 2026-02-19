print("Hej laddvärlden 🚗⚡")
from datetime import datetime
import pytz
import charger

sweden = pytz.timezone("Europe/Stockholm")

plug_connected = True
charge_level = int (input("Write current charging level: "))

while True:
    try:
        user_input = input("When do you need the car? (YYYY-MM-DD HH:MM): ")
        
        # naive datetime
        needed_naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        
        # Change to swedish time
        needed_time = sweden.localize(needed_naive)
        
        break
        
    except ValueError:
        print("Wrong format! Use YYYY-MM-DD HH:MM")

print("Car needed:", needed_time)

charge_start = input("Write 'Plug in' when plugged in: ")

charge_need = charger.batteryCapacity - charge_level*charger.batteryCapacity/100
time_to_charge = charge_need/charger.charger_power

print(time_to_charge)

if charge_start == "Plug in":
    print("Charger plugged in")
    charger.charging(charge_level, True)





