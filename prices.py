from nordpool import elspot
from datetime import datetime, timedelta
import pytz

sweden = pytz.timezone("Europe/Stockholm")

prices_spot = elspot.Prices(currency='SEK')

today = datetime.now()
tomorrow = today + timedelta(days=1)

# Today's data
prices_today = prices_spot.hourly(
    areas=['SE3'], #area, choose when registration as user FIX (S1-S4)
    end_date=today
)

# Tomorrow's data
prices_tomorrow = prices_spot.hourly(
    areas=['SE3'], #area, choose when registration as user FIX (S1-S4)
    end_date=tomorrow
)

all_hours = prices_today['areas']['SE3']['values']

# If tomorrow's data is available
if prices_tomorrow is not None:
    all_hours += prices_tomorrow['areas']['SE3']['values']
else:
    print("Tomorrow's prices not available yet.")


now = datetime.now(sweden)
current_hour = now.replace(minute=0, second=0, microsecond=0)



for hour in all_hours:
    
    local_time = hour['start'].astimezone(sweden) #Convert from utc to swedish time
    
    # Filtrera bort timmar som redan varit
    if local_time >= current_hour:
        price_sek_per_kwh = hour['value'] / 1000
        #print(local_time, price_sek_per_kwh)


def prices_to_charge(date_time_car_needed:datetime, hours_to_charge: int):
    available_hours = []

    for hour in all_hours:
    
        local_time = hour['start'].astimezone(sweden) #Convert from utc to swedish time
    
        # Remove hours not availabe to charge
        if local_time >= current_hour and local_time < date_time_car_needed:
            price_sek_per_kwh = hour['value'] / 1000
            available_hours.append((local_time, price_sek_per_kwh))

    
    # Sortera på pris (index 1 i tuple)
    available_hours.sort(key=lambda x: x[1])
    cheapest_hours = available_hours[:hours_to_charge]

    print(cheapest_hours)

    # return hours with lowest prices
    return [hour[0] for hour in cheapest_hours]
            

