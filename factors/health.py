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
    hospitals = hospital(lat, long)
    pharmacies = pharmacy(lat, long)
    dentists = dentist(lat, long)

    print(Fore.CYAN + "\033[1mHEALTHCARE:-\033[0m" + Style.RESET_ALL)
    print(Fore.CYAN + f"Hospitals: {len(hospitals)}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Pharmacies: {len(pharmacies)}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Dentists: {len(dentists)}" + Style.RESET_ALL)

    # Calculate scores
    health_score = (len(hospitals) * const.WEIGHTS['hospital']) + \
                   (len(pharmacies) * const.WEIGHTS['pharmacy']) + \
                   (len(dentists) * const.WEIGHTS['dentist'])
    
    print(Fore.MAGENTA + f"Healthcare Score: {health_score:.2f}" + Style.RESET_ALL)

    return health_score