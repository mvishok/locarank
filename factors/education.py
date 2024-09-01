from factors import const
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
    

def get_education(lat, long, Fore, Style):
    num_schools = len(school(lat, long))
    num_universities = len(university(lat, long))
    num_libraries = len(library(lat, long))

    print(Fore.CYAN + "\033[1mEDUCATION:-\033[0m" + Style.RESET_ALL)
    print(Fore.CYAN + f"Schools: {num_schools}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Universities: {num_universities}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Libraries: {num_libraries}" + Style.RESET_ALL)

    # Calculate the education score
    education_score = (num_schools * const.WEIGHTS['school']) + \
                      (num_universities * const.WEIGHTS['university']) + \
                      (num_libraries * const.WEIGHTS['library'])
    
    print(Fore.MAGENTA + f"Education Score: {education_score:.2f}" + Style.RESET_ALL)

    return education_score