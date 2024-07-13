#!/usr/bin/python3
# import the necessary modules
import csv
from typing import Dict, List
# OOP but at a later time
class Nutrient:
    def __init__(self, food_class: List[str], food_taken: Dict[str, int]):
        self.food_class = food_class
        self.food_taken = food_taken
        
    def calculator(self):
        total = self.meal_intake()
        food_taken = self.food_taken
        """
        for food in food_taken:
            assert(food_taken[food], int)
        """
        for food in food_taken:
            percentage = (food_taken[food] / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")
            """
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
            """

    def meal_intake(self):
        food_taken0 = self.food_taken
        for classes in food_taken0:
            if classes in food_taken0:
                print(f"how many grams of {classes} did the patient consume? ", end = " ")
                self.food_taken[classes] = int(input())
            else:
                continue
        total = self.food_taken["carbohydrate"] + self.food_taken["protein"] + self.food_taken["fats"] + self.food_taken["vitamins"] + self.food_taken["minerals"] + self.food_taken["roughages"]
        return total
  



    #function that actually reads the nutrients from a csv file
    def read_nutrients_from_csv(self, file_path: str):
            with csv.DictReader(open(file_path)) as csvfile:
                for row in csvfile:
                    for nutrient in self.food_class:
                        if nutrient in row:
                            self.food_taken[nutrient] = int(row[nutrient])
    #function to calculate the nutritional composition of each meal
    
    def save_report_to_csv(self, file_path: str):
        total = sum(self.food_taken.values())
        with open("data.csv", mode='w', newline='') as csvfile:
            fieldnames = ['Nutrient', 'Grams', 'Percentage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for food, amount in self.food_taken.items():
                percentage = (amount / total) * 100
                writer.writerow({'Nutrient': food, 'Grams': amount, 'Percentage': f"{percentage:.2f}%"})

#function that collects the report and saves it into another csv file waiting to be collected by the nutritionist

def main():
    food_taken = {"carbohydrate": 0, "protein": 0, "fats": 0, "vitamins": 0, "minerals": 0, "roughages": 0}
    food_class = ["carbohydrate", "protein", "fats", "vitamins", "minerals", "roughages"]
    item = Nutrient(food_class, food_taken)

    #print(f"The total nutrients consumed in grams is {overall}") #print the total amount of nutrients consumed in grams
    
    item.calculator()
    

if __name__ == "__main__":
    main()