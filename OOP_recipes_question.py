# You have a class of Recipe as follows
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients[:] # create a copy of the list

    def getIngredients(self):
        return self.ingredients[:] # return a copy of ingredients list (following the encapsulation principle and data integrity)


# UMPIRE:
# Understanding:
# 1) Can you give me an example of a Recipe from the Recipe class?
# {'name': 'Chocolate Chip Cookies', 'ingredients': ['Flour', 'Eggs', 'Milk']}

# Match:
# I will use Object Oriented Programming skills and data stucture skills to solve it

# Plan:
# 1) addRecipes() method will add the recipe that I recived by paramiter in a list that it is initialized in the constructor
# 2) getRecipeByIngredient() method will require a new method in the Recipe class because I need to get all the ingredients that each recipe has
# 3) getMostPopularIngredient() method will require more data structure skills. I will create a new hashmap to store the ingredient as the key and a counter as the value, everytime I see this same ingredient, I will update the counter. After that I will traverse this hashmap and see which ingredient has the bigger counter.
# Solve the three methods bellow:

class RecipeRepo:
    def __init__(self):
        self.recipes = []

    def addRecipe(self, recipe):
        self.recipes.append(recipe)
    
    def getRecipeByIngredient(self, ingredient):
        recipes = []
        for recipe in self.recipes:
            if ingredient in recipe.getIngredients():
                recipes.append(recipe)
        return recipes

    def getMostPopularIngredient(self):
        ingredient_count = {}
        for recipe in self.recipes:
            for ingredient in recipe.getIngredients():
                if ingredient in ingredient_count:
                    ingredient_count[ingredient] += 1
                else:
                    ingredient_count[ingredient] = 1
        
        # Find the most popular ingredient in O(n x m) where n is the number of recipes and m is the average number of ingredients per recipe
        most_popular = max(ingredient_count, key=ingredient_count.get)
        # most_popular = None
        # max_counter = 0
        # With this code below is the same time complexity O(n * m), the only thing is that I am not doing a visible for loop iteration
        # for ingredient, count in ingredient_count.items():
        #     if count > max_counter:
        #         max_counter = count
        #         most_popular = ingredient
        
        return most_popular


brigadeiro = Recipe('Brigadeiro', ['Condensed Milk', 'Butter', 'Chocolate Poweder'])
chocolate_cookie = Recipe('Chocolate Chip Cookie', ['Flour', 'Chocolate Chip', 'Butter'])

recipe_repo = RecipeRepo()

recipe_repo.addRecipe(brigadeiro)
recipe_repo.addRecipe(chocolate_cookie)

print(recipe_repo.getMostPopularIngredient())

butter_recipes = recipe_repo.getRecipeByIngredient('Butter')

for recipe in butter_recipes:
    print(f'Recipe 1:', recipe.name)
