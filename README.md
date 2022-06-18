# GET METHODS

/recipes --> Returns an array containing all recipe JSON objects

/recipes/<string:name> --> Returns the specified recipe JSON object if its inside database else return empty JSON object

#TRY "/recipes/beijing-beef"

/recipes/search --> Returns an array of recipe JSON objects that meet the passed parameters

#TRY /recipes/search?complexity=4
#TRY /recipes/search?country=colombia
#TRY /recipes/search?ingredients=water,salt,masarepa,unsalted butter,low moisture mozarella
#TRY /recipes/search?complexity=4&country=colombia
#TRY /recipes/search?complexity=4&country=colombia&ingredients=water,salt,masarepa,unsalted butter,low moisture mozarella

# POST METHODS

/recipes --> Posts passed recipe JSON object into database

#TRY { "name": "beijing-beef", "servings": "3", "mealType": "lunch", "ingredients": ["1.5 (680g) lbs flank steak, cut into 1/2 inch strips", "salt and pepper to taste", "1/2 (under 1g) teaspoon white pepper", "1inch knob ginger, grated", "1/2 (70g) cup cornstarch", "3/4 (113g) cup flour", "1-quart (946ml) vegetable oil", "1 egg", "1.5 tablespoon (22g) water", "1 tablespoon (28g) dark soy", "1 tablespoon (14g) light soy", "1/3 cup (79ml) hoisin sauce", "2 tablespoons (33g) ketchup", "2 tablespoons (33g) sriracha", "1 tablespoon (15g) Chinese black vinegar", "2 tablespoons  (27g) white vinegar", "1/4 cup (57g) sugar", "3 cloves garlic, finely chopped", "3 tablespoons (30g) Vegetable oil", "1 yellow onion cut into 1-inch pieces", "1 red bell pepper cut into 1-inch pieces", "1/2 teaspoon (2g) Sichuan peppercorns, finely ground", "2 teaspoons (5g) corn starch", "1/2 cup water (118ml), plus 2 teaspoons for cornstarch slurry"], "rawIngredients": ["flank steak", "salt", "pepper", "white pepper", "ginger", "cornstarch", "flour", "vegetable oil", "egg", "water", "dark soy", "light soy", "hoisin sauce", "ketchup", "sriracha", "chinese black vinegar", "white vinegar", "sugar", "garlic", "yellow onion", "red bell pepper", "sichuan peppercorns"], "instructions": ["In a medium bowl, add beef, season it with salt to taste, white pepper, and ginger; toss together to combine.", "In a separate medium bowl, combine cornstarch and flour and a generous pinch of salt.  In batches, add your marinated beef to the eggwash; then, to your flour mix, shake off the excess, and place it on a baking sheet.", "To a wok, add oil and preheat it to 350F. Land 2 to 3 pieces of beef at a time, laying away from you to avoid splashing yourself with hot oil.", "Fry for about 4 to 5 minutes or until crispy; remove with a spider drain on a wire rack.  Repeat with the rest of the beef.", "In a medium bowl, mix ½  cup of water, sugar, light soy, dark soy, white vinegar, ketchup, sriracha, hoisin, Sichuan pepper, and Chinese vinegar (optional), till combined; reserve.", "For the slurry, in a small bowl, combine corn starch with 2 tsp of water and mix to combine; reserve.", "In a wok, add enough oil to coat the bottom, add your onion and red bell pepper, season them with salt, stir fry for about 4 minutes; then add the sauce and reduce for two minutes.", "Add slurry incrementally till it gets a thicker consistency, then add fried beef and stir fry for one minute until everything gets coated with the sauce. Cut the heat, add garlic, and serve over medium rice."], "complexity": 4, "country": "China" }

# PUT METHODS

/recipes/<string:name> --> Puts passed recipe JSON object into database

#TRY (COUNTRY IS CHANGED FROM CHINA TO UNITED STATES) 
#PATH = /recipes/beijing-beef 
#BODY = { "name": "beijing-beef", "servings": "3", "mealType": "lunch", "ingredients": ["1.5 (680g) lbs flank steak, cut into 1/2 inch strips", "salt and pepper to taste", "1/2 (under 1g) teaspoon white pepper", "1inch knob ginger, grated", "1/2 (70g) cup cornstarch", "3/4 (113g) cup flour", "1-quart (946ml) vegetable oil", "1 egg", "1.5 tablespoon (22g) water", "1 tablespoon (28g) dark soy", "1 tablespoon (14g) light soy", "1/3 cup (79ml) hoisin sauce", "2 tablespoons (33g) ketchup", "2 tablespoons (33g) sriracha", "1 tablespoon (15g) Chinese black vinegar", "2 tablespoons  (27g) white vinegar", "1/4 cup (57g) sugar", "3 cloves garlic, finely chopped", "3 tablespoons (30g) Vegetable oil", "1 yellow onion cut into 1-inch pieces", "1 red bell pepper cut into 1-inch pieces", "1/2 teaspoon (2g) Sichuan peppercorns, finely ground", "2 teaspoons (5g) corn starch", "1/2 cup water (118ml), plus 2 teaspoons for cornstarch slurry"], "rawIngredients": ["flank steak", "salt", "pepper", "white pepper", "ginger", "cornstarch", "flour", "vegetable oil", "egg", "water", "dark soy", "light soy", "hoisin sauce", "ketchup", "sriracha", "chinese black vinegar", "white vinegar", "sugar", "garlic", "yellow onion", "red bell pepper", "sichuan peppercorns"], "instructions": ["In a medium bowl, add beef, season it with salt to taste, white pepper, and ginger; toss together to combine.", "In a separate medium bowl, combine cornstarch and flour and a generous pinch of salt.  In batches, add your marinated beef to the eggwash; then, to your flour mix, shake off the excess, and place it on a baking sheet.", "To a wok, add oil and preheat it to 350F. Land 2 to 3 pieces of beef at a time, laying away from you to avoid splashing yourself with hot oil.", "Fry for about 4 to 5 minutes or until crispy; remove with a spider drain on a wire rack.  Repeat with the rest of the beef.", "In a medium bowl, mix ½  cup of water, sugar, light soy, dark soy, white vinegar, ketchup, sriracha, hoisin, Sichuan pepper, and Chinese vinegar (optional), till combined; reserve.", "For the slurry, in a small bowl, combine corn starch with 2 tsp of water and mix to combine; reserve.", "In a wok, add enough oil to coat the bottom, add your onion and red bell pepper, season them with salt, stir fry for about 4 minutes; then add the sauce and reduce for two minutes.", "Add slurry incrementally till it gets a thicker consistency, then add fried beef and stir fry for one minute until everything gets coated with the sauce. Cut the heat, add garlic, and serve over medium rice."], "complexity": 4, "country": "United States" } 

# DELETE METHODS

/recipes/<string:name> --> Deletes passed recipe JSON object into database

#TRY /recipes/beijing-beef