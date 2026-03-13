#pull data from meteostat, grabs previous 5 years of weathe data from a specific city

import pandas as pd
from geocoder import Geocoder
from datetime import date
from station_finder import StationFinder
from weather_loader import WeatherLoader


def main():

    # get city from user (US for now)
    city = input('Enter a city: ').strip()

    # convert city to coords
    geocoder = Geocoder()
    coords = geocoder.city_to_coords(city)

    if not coords:
        print("City not found")
        return
    
    lat, lon = coords
    print(f"Coordinates: {lat}, {lon}")

    # find nearby weather stations
    station_finder = StationFinder()
    stations = station_finder.get_near_by_stations(lat, lon)

    print(stations)

    # select closest station

    # load weather data


if __name__ == "__main__":
    main()

