import requests
from urllib.parse import unquote
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# API key
API_KEY = "e1d8a4844b9f4e9588d3177c5b98adf2"

@app.route("/home")
def home():
    return render_template("index.html", recipes = [], search_query = '')

# Define the main roure for the APP
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('search_query', '')
        recipes = search_recipes(query)

        return render_template("index.html", recipes = recipes, search_query = query)
    search_query = request.ars.get('search_query','')
    decoded_search_query = unquote(search_query)
    recipes = search_recipes(decoded_search_query)
    return render_template('index.html, recipes = recipes, search_query = decoded_search_query)')

def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

# Sending a GET request to the spoonacular API

if __name__ == '__main__':
    app.run(debug=True)
