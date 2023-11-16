# Have an application where user can enter the amount of certain foods users have and how many days the user am splitting them between and how many meals each day
# A user will pick the weight of each food that they have 
# The application will calculate how many calories are in that weight of food based off online food api calls
# The application will calculate the meal caloric intake from the food calories and the days and meals that they are split between
# The application will calculate the the daily caloric intake
# Food examples: Chicken Breast, White Rice, Raw Broccoli


import noms


def get_api_key():
    return open("myapikey.txt", "r").read()

def get_food_info(food_name, weight):
    api_key = get_api_key()
    client = noms.Client(api_key)

    def iterativeSearch(result_dict, weight, num):
        try:
            return num, client.get_foods({result_dict['items'][num]["fdcId"] : weight})
        except:
            return iterativeSearch(result_dict, weight, num + 1)
    
    try:
        search_results = client.search_query(food_name)
        result_dict = search_results.json
        food_item = iterativeSearch(result_dict, weight, 0)
        food_description = result_dict['items'][food_item[0]]["description"]
        print(f"Best match found for {food_name} is the food with the description {food_description}")
        meal = noms.Meal(food_item[1])
        r = noms.report(meal)
        return{
            'calories': r[3]["value"],
            'fat': r[1]["value"],
            'protein': r[0]["value"],
            'carbs': r[2]["value"]
        }
    except: 
        print(f"No match found for {food_name}")
        return None

def calculate_meal_intake(foods: dict, days:int, meals:int):
    total_calories = 0
    total_fat = 0
    total_protein = 0
    total_carbs = 0
    for food, weight in foods.items():
        food_info = get_food_info(food, weight)
        if food_info is not None:
            total_calories += (food_info['calories'])
            total_fat += (food_info['fat'])
            total_protein += (food_info['protein'])
            total_carbs += (food_info['carbs'])
    
    meal_caloric_intake = total_calories / (days * meals)
    meal_fat_intake = total_fat / (days * meals)
    meal_protein_intake = total_protein / (days * meals)
    meal_carb_intake = total_carbs / (days * meals)
    
    return meal_caloric_intake, meal_fat_intake, meal_protein_intake, meal_carb_intake


def main():
    foods = {}
    num_foods = int(input("Enter the number of different foods: "))
    for _ in range(num_foods):
        food_name = input("Enter the food name: ")
        food_weight = float(input("Enter the weight of the food (in grams): "))
        foods[food_name] = food_weight
    
    num_days = int(input("Enter the number of days: "))
    num_meals = int(input("Enter the number of meals per day: "))
    
    meal_caloric_intake, meal_fat_intake, meal_protein_intake, meal_carb_intake = calculate_meal_intake(foods, num_days, num_meals)
    print(f"\n\n______________________________________________________________")
    print(f"                          Meal Details")
    print(f"______________________________________________________________")
    print(f"The per meal caloric intake is: {meal_caloric_intake} calories")
    print(f"The per meal fat intake is: {meal_fat_intake} grams")
    print(f"The per meal protein intake is: {meal_protein_intake} grams")
    print(f"The per meal carbohydrate intake is: {meal_carb_intake} grams")

    print(f"\n\n______________________________________________________________")
    print(f"                        Daily Details")
    print(f"______________________________________________________________")
    print(f"The daily caloric intake is: {meal_caloric_intake * num_meals} calories")
    print(f"The daily fat intake is: {meal_fat_intake * num_meals} grams")
    print(f"The daily protein intake is: {meal_protein_intake * num_meals} grams")
    print(f"The daily carbohydrate intake is: {meal_carb_intake * num_meals} grams")

if __name__ == '__main__':
    main()