import const
import requests

def school(lat, long):
    osm_education_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="school"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_education_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def university(lat, long):
    osm_education_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="university"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_education_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    
def library(lat, long):
    osm_education_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="library"](around:{const.RADIUS},{lat},{long});out;'
    response = requests.get(osm_education_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []
    

def get_education(lat, long):
    num_schools = len(school(lat, long))
    num_universities = len(university(lat, long))
    num_libraries = len(library(lat, long))

    # Calculate the education score
    education_score = (num_schools * const.WEIGHTS['school']) + \
                      (num_universities * const.WEIGHTS['university']) + \
                      (num_libraries * const.WEIGHTS['library'])

    return education_score