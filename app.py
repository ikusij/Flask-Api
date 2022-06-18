from flask import Flask, jsonify, request
app = Flask(__name__)

from modules.file_management import read, post, put, delete
from modules.utility import all_ingredients

@app.route("/")
def hello():
    return "Hello World!"

# GET METHODS

@app.route("/recipes", methods = ['GET'])
def get_all_recipes(): 
    
    """Returns an array containing all recipe JSON objects"""
    
    recipes = read()["recipes"]
    return jsonify(recipes)

@app.route("/recipes/<string:name>", methods = ['GET'])
def get_recipe_by_name(name): 

    """Returns the specified recipe JSON object if its inside database else return empty JSON object"""
    
    recipes = read()["recipes"]

    for recipe in recipes:
        if recipe["name"] == name:
            return jsonify(recipe)

    return jsonify({})

@app.route("/recipes/search", methods = ['GET'])
def get_recipe_by_filters():

    """Returns an array of recipe JSON objects that meet the passed parameters"""
    
    recipes = read()["recipes"]
    args = request.args

    if args.get("complexity"): # At most complexity
        query = int(args.get("complexity"))
        recipes = list(filter(lambda recipe: recipe["complexity"] <= query, recipes))
    if args.get("country"): # Exact country
        query = args.get("country").lower()
        recipes = list(filter(lambda recipe: recipe["country"] == query, recipes))
    if args.get("ingredients"): # All ingredients present
        query = args.get("ingredients").split(",")
        recipes = list(filter(lambda recipe: all_ingredients(recipe["rawIngredients"], query), recipes))
    if args.get("mealType"): # Exact meal type
        query = args.get("ingredients").lower()
        recipes = list(filter(lambda recipe: recipe["mealType"] == query, recipes))
    
    return jsonify(recipes)

# POST METHODS

@app.route("/recipes/", methods = ['POST'])
def post_recipe():

    """Posts passed recipe JSON object into database"""

    recipe = request.get_json()
    post(recipe)
    return jsonify(recipe)

# PUT METHODS
@app.route("/recipes/<string:name>", methods = ['PUT'])
def update_recipe(name):

    """Puts passed recipe JSON object into database"""

    recipe = request.get_json()
    put(name, recipe)
    return jsonify(recipe)

# DELETE METHODS
@app.route("/recipes/<string:name>", methods = ['DELETE'])
def delete_recipe(name):

    """Deletes passed recipe JSON object into database"""

    delete(name)
    return jsonify({})