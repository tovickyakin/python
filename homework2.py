# INSTRUCTIONS 
# Create a Program that calculates the Calorie Count for Food
# Steps
# Ask the user for grams of Protein, Carbs and Fat
# Calculate the Calorie value.
# How to Calculate Calories
# A gram of protein is estimated to contain about 4 calories.
# A gram of carbohydrates also has 4, and a gram of fat is worth a whopping 9 calories.
# If the item you’re eating contains 20g of protein, 35g of carbs, and 15g of fat, this means you would multiply 20x4, 35x4, and 15x9 to find the number of calories contributed by each macronutrient—80, 140, and 135, respectively.

protien=int(input("How many grams of Protien is in your food?:\n"))
fat=int(input("How many grams of fat is in your food?:\n"))
carbs=int(input("How many grams of Carbohydrates are in your food?:\n"))



sum=float(carbs*4) + (fat*9) + (protien*4)
print(f"There are {sum} calories in your food")