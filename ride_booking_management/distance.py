import json
import math

def extract_lat_lng(geo_json):
    if not geo_json:
        return None, None
    data = json.loads(geo_json)
    coordinates = data["features"][0]["geometry"]["coordinates"]
    lng = coordinates[0]
    lat = coordinates[1]
    return lat, lng


def calculate_distance(pickup, drop):
    lat1, lng1 = extract_lat_lng(pickup)
    lat2, lng2 = extract_lat_lng(drop)
    if None in (lat1, lng1, lat2, lng2):
        return 0
    R = 6371 
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlng / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return round(distance, 2)