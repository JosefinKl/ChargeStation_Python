from nordpool import elspot
from datetime import datetime
import pytz

sweden = pytz.timezone("Europe/Stockholm")

prices_spot = elspot.Prices(currency='SEK')

prices = prices_spot.hourly(
    areas=['SE3'],  #area, choose when registration as user FIX (S1-S4)
    end_date=datetime.now()
)

for hour in prices['areas']['SE3']['values']:
    
    local_time = hour['start'].astimezone(sweden) #Convert from utc to swedish time

    price_sek_per_kwh = hour['value'] / 1000

    print(local_time, price_sek_per_kwh)