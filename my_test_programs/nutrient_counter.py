#!/usr/bin/python3
# import the necessary modules
# OOP but at a later time
class Nutrient:
    def __init__(self, ):
        pass
    
#function to calculate the nutritional composition of each meal
def meal_intake(carbohydrate = 0, protein = 0, fats = 0, vitamins = 0, mineral = 0, roughages = 0):
    total = carbohydrate + protein + fats + vitamins + mineral + roughages
    return total

def calculator(food_taken, total):
    for food in food_taken:
        if food == "carbohydrate":
            percentage = (food_taken["carbohydrate"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
        elif food == "protein":
            percentage = (food_taken["protein"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
        elif food == "fats":
            percentage = (food_taken["fats"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
        elif food == "vitamins":
            percentage = (food_taken["vitamins"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
        elif food == "minerals":
            percentage = (food_taken["minerals"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
        elif food == "roughages":
            percentage = (food_taken["roughages"] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")

def calc(value):
    total = 0
    for iter in value:
        total = total + value[iter]
    return total

#function that actually reads the nutrients from a csv file

#function that collects the report and saves it into another csv file waiting to be collected by the nutritionist

def main():
    food_taken0 = {"carbohydrate": 0, "protein": 0, "fats": 0, "vitamins": 0, "minerals": 0, "roughages": 0}
    food_class = ["carbohydrate", "protein", "fats", "vitamins", "minerals", "roughages"]
    for classes in food_class:
        if classes in food_taken0:
            print(f"how many grams of {classes} did the patient consume? ", end = " ")
            food_taken0[classes] = int(input())
        else:
            continue
    overall = calc(food_taken0)
    print(f"The total nutrients consumed in grams is {overall}") #print the total amount of nutrients consumed in grams
    calculator(food_taken0, overall)

if __name__ == "__main__":
    main()