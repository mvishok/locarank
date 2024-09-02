import csv
import math
import colorama
from colorama import Fore, Style
from factors import const, education, finance, health, entertainment
import statistics

colorama.init(autoreset=True)

# Example mapping of cities to their latitude and longitude
city_coordinates = {
    "Agra": (27.1767, 78.0081),
    "Ahmedabad": (23.0225, 72.5714),
    "Allahabad": (25.4358, 81.8463),
    "Amritsar": (31.6340, 74.8723),
    "Asansol": (23.6820, 86.9860),
    "Aurangabad": (19.8762, 75.3433),
    "Bengaluru": (12.9716, 77.5946),
    "Bhopal": (23.2599, 77.4126),
    "Chandigarh City": (30.7333, 76.7794),
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Delhi (City)": (28.6139, 77.2090),
    "Dhanbad": (23.7967, 86.4356),
    "Durg-Bhilainagar": (21.2167, 81.2833),
    "Faridabad": (28.4082, 77.3178),
    "Ghaziabad": (28.6692, 77.4538),
    "Gwalior": (26.2183, 78.1828),
    "Hyderabad": (17.3850, 78.4867),
    "Indore": (22.7196, 75.8577),
    "Jabalpur": (23.1815, 79.9559),
    "Jaipur": (26.9124, 75.7873),
    "Jamshedpur": (22.8050, 86.2070),
    "Jodhpur": (26.2950, 73.0169),
    "Kannur": (11.8727, 75.3704),
    "Kanpur": (26.4499, 80.3319),
    "Kochi": (9.9312, 76.2673),
    "Kolkata": (22.5726, 88.3639),
    "Kollam": (8.8910, 76.6141),
    "Kota": (25.2138, 75.8689),
    "Kozhikode": (11.2588, 75.7804),
    "Lucknow": (26.8467, 80.9462),
    "Ludhiana": (30.9010, 75.8573),
    "Madurai": (9.9251, 78.1198),
    "Malappuram": (11.1130, 76.0742),
    "Meerut": (28.9845, 77.7060),
    "Mumbai": (19.0760, 72.8777),
    "Nagpur": (21.1458, 79.0882),
    "Nasik": (19.9975, 73.7898),
    "Patna": (25.5941, 85.1376),
    "Pune": (18.5204, 73.8567),
    "Raipur": (21.2514, 81.6296),
    "Rajkot": (22.3039, 70.8022),
    "Ranchi": (23.3441, 85.3096),
    "Srinagar": (34.0836, 74.7973),
    "Surat": (21.1702, 72.8311),
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Thrissur": (10.5276, 76.2144),
    "Tiruchirapalli": (10.7905, 78.7047),
    "Vadodara": (22.3072, 73.1812),
    "Varanasi": (25.3176, 82.9739),
    "Vasai Virar": (19.2963, 72.8347),
    "Vijayawada": (16.5062, 80.6480),
    "Vishakhapatnam": (17.6868, 83.2185)
}

import csv
import math
import colorama

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two points on the Earth (specified in decimal degrees).
    """
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def fetch_crime_data_from_file(file_path):
    
    #Fetch crime data from the local CSV file and return it as a list of dictionaries.
    
    crime_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            crime_data.append(row)
    return crime_data

def find_nearest_city(lat, lon, city_coordinates):
    
    #Find the nearest city to the given latitude and longitude using Haversine formula.
    
    nearest_city = None
    min_distance = float('inf')
    
    for city, (city_lat, city_lon) in city_coordinates.items():
        distance = haversine(lat, lon, city_lat, city_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_city = city

    return nearest_city

def get_crime_rate_for_city(city_name, crime_data):
     #Get the 'crime' for a specific city from the crime data.
    for data in crime_data:
        if data['city'].strip().lower() == city_name.lower():
            try:
                return float(data['crime'])
            except (KeyError, ValueError) as e:
                print(f"Error parsing crime rate for city: {city_name}, Error: {e}")
                return None
    return None

def classify_safety(crime_rate, median_crime_rate):
    # Calculate the difference from the median
    deviation = crime_rate - median_crime_rate

    # Classification based on deviation
    if deviation <= -100:
        return "Very Safe"
    elif -100 < deviation <= -50:
        return "Safe"
    elif -50 < deviation <= -10:
        return "Moderately Safe"
    elif -10 < deviation <= 10:
        return "Average"
    elif 10 < deviation <= 50:
        return "Moderately Unsafe"
    elif 50 < deviation <= 100:
        return "Unsafe"
    else:
        return "Very Unsafe"

def calculate_median_crime_rate(crime_data):
    # Extract the crime rates from the dataset
    crime_rates = [
        float(data['crime'])
        for data in crime_data
        if data['crime'].replace('.', '', 1).isdigit()
    ]
    return statistics.median(crime_rates)

def get_safety(lat, long, fore, style):
    crime_data = fetch_crime_data_from_file('C:\\Users\\mmani\\Desktop\\locarank\\factors\\crimerate.csv')
    median_crime_rate = calculate_median_crime_rate(crime_data)
    nearest_city = find_nearest_city(lat, long, city_coordinates)
    crime_rate = get_crime_rate_for_city(nearest_city, crime_data) if nearest_city else None

    if crime_rate is not None:
        deviation = crime_rate - median_crime_rate

        # Classification based on deviation
        if deviation <= -200:
            return 1
        elif -200 < deviation <= -100:
            return 0.8
        elif -100 < deviation <= -50:
            return 0.7
        elif -50 < deviation <= 0:
            return 0.6
        elif 0 < deviation <= 50:
            return 0.5
        elif 50 < deviation <= 200:
            return 0.3
        else:
            return 0.1
    else:
        print(f"{fore}Crime rate not available for the nearest city.")
        return 0