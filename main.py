import requests

# Define the latitude and longitude for Chennai
latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))

# OpenStreetMap API URLs for hospitals and entertainment
osm_hospitals_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["amenity"="hospital"](around:5000,{latitude},{longitude});out;'
osm_entertainment_url = f'https://overpass-api.de/api/interpreter?data=[out:json];node["leisure"="park"](around:5000,{latitude},{longitude});out;'

# Free weather API URL (Meteosource or OpenWeatherMap)
weather_api_key = 'bd5e378503939ddaee76f12ad7a97608'
weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api_key}&units=metric'

# Function to get hospital data from OpenStreetMap
def get_hospitals():
    response = requests.get(osm_hospitals_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

# Function to get entertainment data from OpenStreetMap
def get_entertainment():
    response = requests.get(osm_entertainment_url)
    if response.status_code == 200:
        return response.json()['elements']
    else:
        return []

# Function to get weather data
def get_weather():
    response = requests.get(weather_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get water availability data (using a hypothetical API or static data)
def get_water_availability():
    # This is a placeholder; you can replace this with actual data fetching logic.
    return {'availability': 'good'}  # Example static response

# Calculate scores for each factor
def calculate_scores():
    hospital_data = get_hospitals()
    entertainment_data = get_entertainment()
    weather_data = get_weather()
    water_data = get_water_availability()

    # Score calculations
    hospital_score = len(hospital_data) * 10
    entertainment_score = len(entertainment_data) * 5

    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_score = (30 - abs(temp - 25)) * 2 - humidity  # Example scoring based on comfort
    else:
        weather_score = 0

    water_score = 20 if water_data['availability'] == 'good' else 0

    print("Hospital Score: ", hospital_score)
    print("Entertainment Score: ", entertainment_score)
    print("Weather Score: ", weather_score)
    print("Water Score: ", water_score)

    return {
        'hospital_score': hospital_score,
        'entertainment_score': entertainment_score,
        'weather_score': weather_score,
        'water_score': water_score
    }

# Generate the overall rank
def generate_rank():
    scores = calculate_scores()
    overall_score = (
        scores['hospital_score'] * 0.4 +
        scores['entertainment_score'] * 0.2 +
        scores['weather_score'] * 0.2 +
        scores['water_score'] * 0.2
    )
    return overall_score

# Example usage
if __name__ == "__main__":
    rank = generate_rank()
    print(f'The rank for the given location is: {rank}')