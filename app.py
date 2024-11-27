from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Spoonacular API configuration
API_KEY = "e1d8a4844b9f4e9588d3177c5b98adf2"
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

@app.route('/')
def home():
    return render_template('home.html')  # Home page where the user inputs ingredients

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients').split(',')
        params = {
            "apiKey": API_KEY,
            "includeIngredients": ','.join(ingredients),
            "number": 5  # Limit to 5 results
        }
        response = requests.get(BASE_URL, params = params)
        if response.status_code == 200:
            recipes = response.json().get('results', [])
            return render_template('results.html', recipes = recipes)
        else:
            # If the API call fails, print the error
            return f"Error fetching data from Spoonacular API: {response.status_code}", 500

            # In case of GET request or empty form, redirect back to home
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
