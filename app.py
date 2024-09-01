import colorama
from colorama import Fore, Style
import factors.const as const
from factors import education, finance, health, entertainment
from flask import Flask, request

colorama.init(autoreset=True)

def calculate_total_score(scores):
    total_score = 0

    for category, score in scores.items():
        weight = const.CATEGORY.get(category, 0)
        total_score += score * weight

    return total_score

app = Flask(__name__)

@app.route('/score')
def score():

    if 'latitude' not in request.args or 'longitude' not in request.args:
        return 'Error: Please provide both latitude and longitude.', 400

    # get the latitude and longitude from the query parameters
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    category_scores = {
        'Education': education.get_education(latitude, longitude, Fore, Style),
        'Healthcare': health.get_health(latitude, longitude, Fore, Style),
        'Finance': finance.get_finance(latitude, longitude, Fore, Style),
        'Entertainment': entertainment.get_entertainment(latitude, longitude, Fore, Style)
    }

    total_score = calculate_total_score(category_scores)

    result = {
        'total_score': total_score,
        'category': category_scores
    }

    return result

    

if __name__ == '__main__':
    app.run(debug=True)