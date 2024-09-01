import const
import requests

# Weights
weight_school = 1.0
weight_university = 2.0
weight_library = 0.5

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
    education_score = (num_schools * weight_school) + \
                      (num_universities * weight_university) + \
                      (num_libraries * weight_library)

    return education_score