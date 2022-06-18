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
    recipes = read()["recipes"]
    return jsonify(recipes)

@app.route("/recipes/<string:name>", methods = ['GET'])
def get_recipe_by_name(name): 
    
    recipes = read()["recipes"]

    for recipe in recipes:
        if recipe["name"] == name:
            return jsonify(recipe)

    return jsonify({})

@app.route("/recipes/search", methods = ['GET'])
def get_recipe_by_filters():
    
    recipes = read()["recipes"]
    args = request.args

    if args.get("complexity"):
        query = int(args.get("complexity"))
        recipes = list(filter(lambda recipe: recipe["complexity"] <= query, recipes))
    if args.get("country"):
        query = args.get("country").lower()
        recipes = list(filter(lambda recipe: recipe["country"] == query, recipes))
    if args.get("ingredients"):
        query = args.get("ingredients").split(",")
        recipes = list(filter(lambda recipe: all_ingredients(recipe["rawIngredients"], query), recipes))
    if args.get("mealType"):
        query = args.get("ingredients").lower()
        recipes = list(filter(lambda recipe: recipe["mealType"] == query, recipes))
    
    return jsonify(recipes)

# POST METHODS

@app.route("/recipes/", methods = ['POST'])
def post_recipe():

    recipe = request.get_json()
    post(recipe)
    return jsonify(recipe)

# PUT METHODS
@app.route("/recipes/<string:name>", methods = ['PUT'])
def update_recipe(name):

    recipe = request.get_json()
    put(name, recipe)
    return jsonify(recipe)

# DELETE METHODS
@app.route("/recipes/<string:name>", methods = ['DELETE'])
def delete_recipe(name):
    delete(name)
    return jsonify({})