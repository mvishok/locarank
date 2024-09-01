import const
import requests

# Assign weights
hospital_weight = 5
pharmacy_weight = 3
dentist_weight = 2

def hospital(lat, long):
    osm_health_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="hospital"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_health_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

def pharmacy(lat, long):
    osm_health_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="pharmacy"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_health_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def dentist(lat, long):
    osm_health_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="dentist"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_health_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

def get_health(lat, long):
    # Fetch health facilities
    hospitals = hospital(lat, long)
    pharmacies = pharmacy(lat, long)
    dentists = dentist(lat, long)

    # Calculate scores
    health_score = (len(hospitals) * hospital_weight) + \
                   (len(pharmacies) * pharmacy_weight) + \
                   (len(dentists) * dentist_weight)

    return health_score