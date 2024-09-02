import requests
from factors import const

def bank(lat, long):
    osm_finance_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="bank"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_finance_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def atm(lat, long):
    osm_finance_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="atm"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_finance_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def get_finance(lat, long, Fore, Style):
    banks = len(bank(lat, long))
    atms = len(atm(lat, long))

    print(Fore.CYAN + "\033[1mFINANCE:-\033[0m" + Style.RESET_ALL)
    print(Fore.CYAN + f"Banks: {banks}" + Style.RESET_ALL)
    print(Fore.CYAN + f"ATMs: {atms}" + Style.RESET_ALL)

    if banks > 50: banks = 50
    if atms > 60: atms = 60

    # Calculate scores
    finance_score = (banks * const.WEIGHTS['bank']) + (atms * const.WEIGHTS['atm'])

    print(Fore.MAGENTA + f"Finance Score: {finance_score:.2f}" + Style.RESET_ALL)

    return finance_score