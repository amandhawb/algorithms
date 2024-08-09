# You have a class of Recipe as follows (Java):
# class Recipe {
    # Recipe(String name, List<String> ingredients) {
        # List <String> getIngredients() {

            # }
    #  }
  # }

# Solve the three methods bellow:

# interface RecipeRepo {
    # void addRecipe(Recipe recipe):
    # List<Recipe> getRecipeByIngredient(Ingredient ingredient):
    # String getMostPopularIngredient();
# }

# Understanding:
# 1) Can you give me an example of a Recipe from the Recipe class?
# {'name': 'Chocolate Chip Cookies', 'ingredients': ['Flour', 'Eggs', 'Milk']}

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients[:]
    
    def get_ingredients(self):
        return self.ingredients[:]

# class RecipeRepoInterface:
#     def addRecipe(self, recipe):
#         return None

#     def getRecipeByIngredient(self, ingredient):
#         return None

#     def getMostPopularIngredient(self):
#         return None
    
class Controller:
    def __init__(self):
        self.recipes = []
    
    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def print_recipes(self):
        for recipe in self.recipes:
            print(recipe.name)
            print(recipe.ingredients)

    def getRecipeByIngredient(self, ingredient):
        result = []
        for recipe in self.recipes:
            if ingredient in recipe.get_ingredients():
                result.append(recipe)
        return result

    def getMostPopularIngredient(self):
        ingredient_count = {}
        for recipe in self.recipes:
            for ingredient in recipe.get_ingredients():
                if ingredient in ingredient_count:
                    ingredient_count[ingredient] += 1
                else:
                    ingredient_count[ingredient] = 1

        most_pupular = None
        max_counter = 0
        for ingredient, counter in ingredient_count.items():
            if counter > max_counter:
                max_counter = counter
                most_pupular = ingredient
        
        return most_pupular


chocolate_chip_cookie = Recipe("Chocolate Chip Cookies", ["Flour", "Eggs", "Milk"])

controller = Controller()
controller.add_recipe(chocolate_chip_cookie)
brigadeiro = Recipe("Brigadeiro", ["Condensed milk", "Chocolate Powder", "Butter", "Milk"])
controller.add_recipe(brigadeiro)
controller.print_recipes()


milk_recipes = controller.getRecipeByIngredient('Milk')

for index, recipe in enumerate(milk_recipes):
    print(f'Recipe {index + 1}:', recipe.name)

print(controller.getMostPopularIngredient(), 'aqui')




