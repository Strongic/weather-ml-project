from geopy.geocoders import Nominatim

class Geocoder:
    def __init__(self):
        self.geolocator = Nominatim(user_agent='weather-ml-locator')

    def city_to_coords(self, city):
        location = self.geolocator.geocode(city)
        
        if not location:
            return None

        return location.latitude, location.longitude