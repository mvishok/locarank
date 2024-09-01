import const
import requests

# Weights for each entertainment category

park_weight = 2
theatre_weight = 4
museum_weight = 3
cinema_weight = 4
art_gallery_weight = 3
zoo_weight = 5
playground_weight = 2
sports_centre_weight = 4
swimming_pool_weight = 3

# -------------

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


def get_entertainment_score(lat, long):
    park_count = len(park(lat, long))
    theatre_count = len(theatre(lat, long))
    museum_count = len(museum(lat, long))
    cinema_count = len(cinema(lat, long))
    art_gallery_count = len(art_gallery(lat, long))
    zoo_count = len(zoo(lat, long))
    playground_count = len(playground(lat, long))
    sports_centre_count = len(sports_centre(lat, long))
    swimming_pool_count = len(swimming_pool(lat, long))

    entertainment_score = (
        park_count * park_weight +
        theatre_count * theatre_weight +
        museum_count * museum_weight +
        cinema_count * cinema_weight +
        art_gallery_count * art_gallery_weight +
        zoo_count * zoo_weight +
        playground_count * playground_weight +
        sports_centre_count * sports_centre_weight +
        swimming_pool_count * swimming_pool_weight
    )

    return entertainment_score