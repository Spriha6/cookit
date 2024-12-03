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
    response = requests.get(url, params=params)
    # if the API call is successful
    if response.status_code == 200:
        #parse the API response as JSON data
        data = response.json()
        # Return the list of recipes
        return data ['results']
        # if API call not successful
    return []

# Get the recipes information
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    search_query = request.arg.get('search_query','')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apikey': API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        return render_template('result.html', recipe = recipe, search_query = search_query)
    return "Recipe not found", 404


if __name__ == '__main__':
    app.run(debug=True)
