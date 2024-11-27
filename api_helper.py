import requests

# Add your Spoonacular API key here
API_KEY = "e1d8a4844b9f4e9588d3177c5b98adf2"
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

def get_recipes(ingredients):
    """
    Fetch recipes from Spoonacular based on the provided ingredients.
    :param ingredients: List of ingredients (e.g., ['tomato', 'cheese'])
    :return: List of recipes
    """
    # Convert ingredients list to a comma-separated string
    query = ','.join(ingredients)

    # Prepare the API request
    params = {
        "apiKey": API_KEY,
        "includeIngredients": query,
        "number": 5,  # Limit results to 5 recipes
    }

    response = requests.get(BASE_URL, params = params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])  # Return the list of recipes
    else:
        # Log and return an empty list on error
        print(f"Error: {response.status_code} - {response.text}")
        return []
