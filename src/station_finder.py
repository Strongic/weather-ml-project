from meteostat import stations

class StationFinder:

    def get_near_by_stations(self, lat, lon, limit=4):

        stations = stations()
        stations = stations.nearby(lat, lon)
        stations = stations.fetch(limit)

        return stations