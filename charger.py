import time

batteryCapacity = 100  # kWh
charger_power = 11     # kW

def charging(charge_level: float):
    plug_connected = True
    
    while plug_connected and charge_level < 100:
        energy_added = charger_power / 60
        charge_level += energy_added / batteryCapacity * 100

        if charge_level >= 100:
            charge_level = 100
            print(f"Charge level: {charge_level:.2f}%")
            break
        
        print(f"Charge level: {charge_level:.2f}%")
        
        time.sleep(1)
        
        # TEST: dra ur sladden manuellt genom att ändra här
        # plug_connected = False
    
    print("Laddning stoppad.")
    return charge_level

print(charging(10))
