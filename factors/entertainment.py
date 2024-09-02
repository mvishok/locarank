from factors import const
import requests

def park(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["leisure"="park"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

# A theatre is a venue for live performances, including plays, musicals, and other stage productions. The focus is on live acting and performances rather than film.
def theatre(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="theatre"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def museum(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["tourism"="museum"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

# A cinema is a venue specifically designed for showing movies (films). It typically features multiple screens and is open to the public for a fee.
def cinema(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="cinema"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

def art_gallery(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["tourism"="art_gallery"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def zoo(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["tourism"="zoo"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def playground(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["leisure"="playground"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def sports_centre(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["leisure"="sports_centre"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def swimming_pool(lat, long):
    osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["leisure"="swimming_pool"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []


def get_entertainment(lat, long, Fore, Style):
    park_count = len(park(lat, long))
    theatre_count = len(theatre(lat, long))
    museum_count = len(museum(lat, long))
    cinema_count = len(cinema(lat, long))
    art_gallery_count = len(art_gallery(lat, long))
    zoo_count = len(zoo(lat, long))
    playground_count = len(playground(lat, long))
    sports_centre_count = len(sports_centre(lat, long))
    swimming_pool_count = len(swimming_pool(lat, long))

    if (park_count > 10): park_count = 10
    if (theatre_count > 10): theatre_count = 10
    if (museum_count > 1): museum_count = 1
    if (cinema_count > 5): cinema_count = 5
    if (art_gallery_count > 3): art_gallery_count = 3
    if (zoo_count > 1): zoo_count = 1
    if (playground_count > 10): playground_count = 10
    if (sports_centre_count > 5): sports_centre_count = 5
    if (swimming_pool_count > 5): swimming_pool_count = 5

    print(Fore.CYAN + "\033[1mENTERTAINMENT:-\033[0m" + Style.RESET_ALL)
    print(Fore.CYAN + f"Parks: {park_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Theatres: {theatre_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Museums: {museum_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Cinemas: {cinema_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Art Galleries: {art_gallery_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Zoos: {zoo_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Playgrounds: {playground_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Sports Centres: {sports_centre_count}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Swimming Pools: {swimming_pool_count}" + Style.RESET_ALL)

    entertainment_score = (
        park_count * const.WEIGHTS['park'] +
        theatre_count * const.WEIGHTS['theatre'] +
        museum_count * const.WEIGHTS['museum'] +
        cinema_count * const.WEIGHTS['cinema'] +
        art_gallery_count * const.WEIGHTS['art_gallery'] +
        zoo_count * const.WEIGHTS['zoo'] +
        playground_count * const.WEIGHTS['playground'] +
        sports_centre_count * const.WEIGHTS['sports_centre'] +
        swimming_pool_count * const.WEIGHTS['swimming_pool']
    )

    print(Fore.MAGENTA + f"Entertainment Score: {entertainment_score:.2f}" + Style.RESET_ALL)

    return entertainment_score