#pull data from meteostat, grabs previous 5 years of weathe data from a specific city

from datetime import date
import meteostat as ms

start = date(2021, 1, 1)
end = date(2025, 12, 31)

ts = ms.daily(ms.Station(id='10637'), start, end)
df = ts.fetch()

print(df)