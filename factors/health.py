from factors import const
import requests

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

def get_health(lat, long, Fore, Style):
    # Fetch health facilities
    hospitals = len(hospital(lat, long))
    pharmacies = len(pharmacy(lat, long))
    dentists = len(dentist(lat, long))

    print(Fore.CYAN + "\033[1mHEALTHCARE:-\033[0m" + Style.RESET_ALL)
    print(Fore.CYAN + f"Hospitals: {hospitals}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Pharmacies: {pharmacies}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Dentists: {dentists}" + Style.RESET_ALL)


    if (hospitals) > 90: hospitals = 90
    if (pharmacies) > 60: pharmacies = 60
    if (dentists) > 10: dentists = 10


    # Calculate scores
    health_score = (hospitals * const.WEIGHTS['hospital']) + \
                   (pharmacies * const.WEIGHTS['pharmacy']) + \
                   (dentists * const.WEIGHTS['dentist'])
    
    print(Fore.MAGENTA + f"Healthcare Score: {health_score:.2f}" + Style.RESET_ALL)

    return health_score