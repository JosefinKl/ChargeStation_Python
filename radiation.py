import requests
from datetime import datetime
import user

url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={user.latitude}&longitude={user.longitude}"
    "&hourly=shortwave_radiation"
    "&forecast_days=2"
    "&timezone=Europe/Stockholm"
)

response = requests.get(url)
data = response.json()

times = data["hourly"]["time"]
sunshine = data["hourly"]["shortwave_radiation"]  #W/m²

#print("Kommande 48h soltimmar:\n")

solar_production = []

tot_solar_production = 0


    
for t, r in zip(times, sunshine):
    dt = datetime.fromisoformat(t)
    

    if r > 0:
        # Effect in kW
        power_kw = user.system_size_kwp * (r / 1000)

        # Comvert to kWh
        energy_kwh = power_kw * 1

        tot_solar_production = tot_solar_production + energy_kwh

        solar_production.append((dt, round(energy_kwh, 2)))
        

print("Beräknad solproduktion kommande 48h:")
print(solar_production)
print(tot_solar_production)