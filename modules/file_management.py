import json

def read(filename: str = './database/database.json') -> dict:
    with open(filename, 'r') as file:
        database = json.load(file)
    return database

def post(json_data: dict, filename: str = './database/database.json') -> None:
    
    database = read(filename)
    recipes = database["recipes"]
    recipes.append(json_data)
    
    with open(filename, 'w') as file:
        json.dump(database, file)

def put(name: str, json_data: dict, filename: str = './database/database.json') -> None:

    database = read(filename)
    recipes = database["recipes"]

    for index, recipe in enumerate(recipes):
        if recipe["name"] == name:
            recipes[index] = json_data
    
    with open(filename, 'w') as file:
        json.dump(database, file)

def delete(name: str, filename: str = './database/database.json') -> None:
    
    database = read(filename)
    recipes = database["recipes"]

    for index, recipe in enumerate(recipes):
        if recipe["name"] == name:
            del recipes[index]
    
    with open(filename, 'w') as file:
        json.dump(database, file)