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

# Both lists
all_hours = (
    prices_today['areas']['SE3']['values'] +
    prices_tomorrow['areas']['SE3']['values']
)


now = datetime.now(sweden)
current_hour = now.replace(minute=0, second=0, microsecond=0)



for hour in all_hours:
    
    local_time = hour['start'].astimezone(sweden) #Convert from utc to swedish time
    
    # Filtrera bort timmar som redan varit
    if local_time >= current_hour:
        price_sek_per_kwh = hour['value'] / 1000
        print(local_time, price_sek_per_kwh)

