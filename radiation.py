import requests
from datetime import datetime

#Coordinates for Stockholm  CHange when makeing it personal for user
latitude = 59.3293
longitude = 18.0686

system_size_kwp = 10  # user sunpanel


url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
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


    
for t, r in zip(times, sunshine):
    dt = datetime.fromisoformat(t)
    

    if r > 0:
        # Effect in kW
        power_kw = system_size_kwp * (r / 1000)

        # Comvert to kWh
        energy_kwh = power_kw * 1

        solar_production.append((dt, round(energy_kwh, 2)))
        

print("Beräknad solproduktion kommande 48h:")
print(solar_production)