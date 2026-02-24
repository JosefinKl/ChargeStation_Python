import requests
from datetime import datetime

#Coordinates for Stockholm  CHange when makeing it personal for user
latitude = 59.3293
longitude = 18.0686


url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    "&hourly=sunshine_duration"
    "&forecast_days=2"
    "&timezone=Europe/Stockholm"
)

response = requests.get(url)
data = response.json()

times = data["hourly"]["time"]
sunshine = data["hourly"]["sunshine_duration"]  # seconds per hour

#print("Kommande 48h soltimmar:\n")

sunshine_list = []



for t, s in zip(times, sunshine):
    dt = datetime.fromisoformat(t)
    hours = s / 3600  # konvert seconds to hours
    
    #print(f"{dt}: {hours:.2f}")

    if hours > 0:
        sunshine_list.append((dt, hours))

print("List of hours the coming 48h with sunshine accoring to wheater forcast")
print(sunshine_list)