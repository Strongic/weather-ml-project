from meteostat import Daily
from datetime import date

class WeatherLoader:

    def get_weather(self, station_id):


        start = date(2020, 1, 1)
        end = date(2025, 1, 1)
        
        data = data(station_id, start, end)
        df = data.fetch()

        return df