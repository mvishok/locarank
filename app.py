import colorama
from colorama import Fore, Style
import factors.const as const
from factors import education, finance, health, entertainment, safety
from flask import Flask, request

from flasgger import Swagger

colorama.init(autoreset=True)

def calculate_total_score(scores):
    total_score = 0

    for category, score in scores.items():
        weight = const.CATEGORY.get(category, 0)
        total_score += score * weight
    
    # map 486.1 to 100
    total_score = (total_score / 486.1) * 100
    
    return total_score

app = Flask(__name__)
app.config['url_sort_key'] = None
app.config['SWAGGER'] = {
    'title': 'LocaRank API',
    'uiversion': 3,
    'hide_top_bar': True,
    'specs_route': '/',
    'static_url_path': '/static',
    'static_folder': 'static',
}

swagger = Swagger(app)

@app.route('/score')
def score():
    """
    Endpoint to get total score for a given latitude and longitude
    ---
    summary: Get total score for a location
    description: This endpoint calculates the total score for a given location based on the latitude and longitude provided.
    consumes:
      - application/json
    parameters:
      - name: latitude
        in: query
        type: number
        required: true
        description: The latitude of the location.
      - name: longitude
        in: query
        type: number
        required: true
        description: The longitude of the location.
    responses:
      200:
        description: The total score and category-wise scores.
        schema:
          id: score
          properties:
            total_score:
              type: number
              description: The total score for the location.
            category:
              type: object
              description: The category-wise scores.
              properties:
                Education:
                  type: number
                  description: The education score.
                Healthcare:
                  type: number
                  description: The healthcare score.
                Finance:
                  type: number
                  description: The finance score.
                Entertainment:
                  type: number
                  description: The entertainment score.
      400:
        description: Error message.
    """

    if 'latitude' not in request.args or 'longitude' not in request.args:
        return 'Error: Please provide both latitude and longitude.', 400

    # get the latitude and longitude from the query parameters
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    category_scores = {
        'Education': education.get_education(latitude, longitude, Fore, Style),
        'Healthcare': health.get_health(latitude, longitude, Fore, Style),
        'Finance': finance.get_finance(latitude, longitude, Fore, Style),
        'Entertainment': entertainment.get_entertainment(latitude, longitude, Fore, Style),
        'Safety': safety.get_safety(latitude, longitude, Fore, Style)
    }

    total_score = calculate_total_score(category_scores)

    result = {
        'total_score': total_score,
        'category': category_scores
    }

    return result

@app.route('/temp')
def temp():
    return {
      "category": {
        "Education": 0.5,
        "Entertainment": 0,
        "Finance": 25,
        "Healthcare": 105,
        "Safety": 0.8
      },
      "total_score": 4.9043406706439
    }
if __name__ == '__main__':
    app.run(debug=True)