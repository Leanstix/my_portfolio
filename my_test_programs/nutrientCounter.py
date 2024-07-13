#!/usr/bin/python3
# import the necessary modules
import csv

from typing import Dict, List
#OOP
class Nutrient:
    def __init__(self, food_class: List[str], food_taken: Dict[str, int]):
        self.food_class = food_class
        self.food_taken = food_taken
        
    
    #function to calculate the nutritional composition of each meal  
    def calculator(self):
        total = self.meal_intake()
        for food, amount in self.food_taken.items():
            percentage = (amount / total) * 100
            print(f"The total gram of {food} taken by patient is {percentage:.2f}%")

    def meal_intake(self) -> int:
        for nutrient in self.food_class:
            if nutrient in self.food_taken:
                self.food_taken[nutrient] = int(input(f"How many grams of {nutrient} did the patient consume? "))
        total = sum(self.food_taken.values())
        return total
    #function that actually reads the nutrients from a csv file
    def read_nutrients_from_csv(self, file_path: str):
        with csv.DictReader(open(file_path, 'r')) as csvfile:
            for row in csvfile:
                for nutrient in self.food_class:
                    if nutrient in row:
                        self.food_taken[nutrient] = int(row[nutrient])
    #function that collects the report and saves it into another csv file waiting to be collected by the nutritionist
    def save_report_to_csv(self, file_path: str):
        total = sum(self.food_taken.values())
        with open(file_path, mode='w', newline='') as csvfile:
            fieldnames = ['Nutrient', 'Grams', 'Percentage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for food, amount in self.food_taken.items():
                percentage = (amount / total) * 100
                writer.writerow({'Nutrient': food, 'Grams': amount, 'Percentage': f"{percentage:.2f}%"})
       

def main():
    food_taken = {"carbohydrate": 0, "protein": 0, "fats": 0, "vitamins": 0, "minerals": 0, "roughages": 0}
    food_class = ["carbohydrate", "protein", "fats", "vitamins", "minerals", "roughages"]
   
    item = Nutrient(food_class, food_taken)

   
    
    item.read_nutrients_from_csv('details.csv')
    item.calculator()
    item.save_report_to_csv('output.csv')
   

if __name__ == "__main__":
    main()
