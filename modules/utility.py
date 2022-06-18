def all_ingredients(recipe_ingredients, available_ingredients):
    for recipe_ingredient in recipe_ingredients:
        if recipe_ingredient not in available_ingredients:
            return False
    return True