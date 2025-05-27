# dorm_meal_recommender.py
# A rule-based system that suggests dorm meals based on available ingredients

def recommend_meal(ingredients):
    ingredients = [item.strip().lower() for item in ingredients.split(",")]

    if "eggs" in ingredients and "bread" in ingredients:
        return "You can make French Toast!"
    elif "rice" in ingredients and "beans" in ingredients:
        return "How about a Rice and Beans Bowl?"
    elif "ramen" in ingredients and "cheese" in ingredients:
        return "Try making some Cheesy Ramen!"
    elif "tortilla" in ingredients and "cheese" in ingredients:
        return "Sounds like a Quesadilla kind of day!"
    else:
        return "Sorry, I don't have a recipe for those ingredients. Try a snack or get takeout."

# Main program
if __name__ == "__main__":
    print("Welcome to the Dorm Meal Recommender!")
    user_input = input("Enter the ingredients you have, separated by commas: ")
    result = recommend_meal(user_input)
    print(result)
