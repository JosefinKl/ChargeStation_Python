print("Hej laddvärlden 🚗⚡")
from datetime import datetime, timedelta
import pytz
import charger
import prices
import time
import math

sweden = pytz.timezone("Europe/Stockholm")
simulated_time = datetime.now(sweden).replace(minute=0, second=0, microsecond=0) #Start with real time

def advance_time():
    global simulated_time
    simulated_time += timedelta(hours=1)

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
time_to_charge = math.ceil(charge_need / charger.charger_power)
print(time_to_charge)

#print(type(time_to_charge))


if charge_start == "Plug in":
    print("Charger plugged in")
    cheapest_hours = prices.prices_to_charge(needed_time, time_to_charge)

    print("Charging will run during:")
    for h in cheapest_hours:
        print(h)

    print("Waiting for cheapest hours...")

    while charge_level < 100 and simulated_time < needed_time:
        print(f"\nSimulated time: {simulated_time}")

        if simulated_time in cheapest_hours:
            print("Cheap hour → Charging ⚡")
            charge_level = charger.charging(charge_level)
        else:
            print("Expensive hour → Waiting")

        time.sleep(1)          # 1 sekund verklig tid
        advance_time()         # +1 timme simulerad tid




