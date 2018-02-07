from geopy.distance import vincenty

def distance_to_soda(lat: float, lon: float) -> float:
    """
    `distance_to_soda(lat, lon)` returns the distance, in miles, of the point
    (lat, lon) from Soda Hall.
    """
    # The latitude and longitude of Soda Hall was found using Google maps.
    soda_lat = 37.875634
    soda_lon = -122.258738
    return vincenty((soda_lat, soda_lon), (lat, lon)).miles
