import time
import threading

batteryCapacity = 100  # kWh
charger_power = 11     # kW
stop_charging = False 

def wait_for_stop():
    global stop_charging
    input("Write 'Stop' to stop charging: ")
    stop_charging = True


def charging(charge_level: float):
    global stop_charging
    
    threading.Thread(target=wait_for_stop, daemon=True).start()

    if charge_level < 100 and not stop_charging :
        energy_added = charger_power #every iteration (takes 1second) corresponds to 1 hour
        charge_level += energy_added / batteryCapacity * 100

        if charge_level >= 100:
            charge_level = 100
            print(f"Charge level: {charge_level:.2f}%")
            
        
        print(f"Charge level: {charge_level:.2f}%")
        
        #time.sleep(1) #sleep for 1 second, hence every iteration takes 1 second. To simulate real time. 
        
       
        
    
    print("Stopped charging." + f"Charge level: {charge_level:.2f}%")
 
    return charge_level


