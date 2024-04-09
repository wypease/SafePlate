from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_profile', methods=['POST'])
def create_profile():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    allergies = data.get('allergies')

    # Process the data as needed (store in a database, etc.)

    # Return the user profile as JSON
    return jsonify({'name': name, 'age': age, 'allergies': allergies})

# Food Search Function route
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_type = data.get('searchType')
    search_input = data.get('searchInput')

    # Implement search logic based on the search type
    # For simplicity, let's just return a list of dummy results
    results = []
    if search_type == 'allergies':
        results = ['Allergy-friendly meal 1', 'Allergy-friendly meal 2']
    elif search_type == 'recipes':
        results = ['Recipe 1', 'Recipe 2']
    elif search_type == 'restaurants':
        results = ['Restaurant 1', 'Restaurant 2']
    elif search_type == 'price':
        results = ['Affordable meal 1', 'Affordable meal 2']

    return jsonify(results)

# Include the following routes for saving recipes and restaurants
saved_recipes = []
saved_restaurants = []

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    data = request.get_json()
    recipe_name = data.get('recipeName')
    if recipe_name not in saved_recipes:
        saved_recipes.append(recipe_name)
    return jsonify({'message': 'Recipe saved successfully'})

@app.route('/save_restaurant', methods=['POST'])
def save_restaurant():
    data = request.get_json()
    restaurant_name = data.get('restaurantName')
    if restaurant_name not in saved_restaurants:
        saved_restaurants.append(restaurant_name)
    return jsonify({'message': 'Restaurant saved successfully'})

built_recipes = []

@app.route('/build_recipe', methods=['POST'])
def build_recipe():
    data = request.get_json()
    recipe_name = data.get('recipeName')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')

    # Assuming a simple validation for now
    if recipe_name and ingredients and instructions:
        recipe = {
            'name': recipe_name,
            'ingredients': ingredients,
            'instructions': instructions
        }
        built_recipes.append(recipe)
        return jsonify({'message': 'Recipe built successfully'})
    else:
        return jsonify({'message': 'Failed to build recipe. Please fill in all fields.'})


if __name__ == '__main__':
    app.run(debug=True)
