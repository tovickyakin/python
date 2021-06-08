# Create a Program to Convert any given values for Miles to Kilometers. Your Answer should be rounded off to 2 Decimal Places.

# Steps
# Ask the user to enter a value for miles
# Calculate the kilometres based on the formula mentioned below
# Hint
# 1 Mile = 1.609 Kilometre

mile=int(input ("Enter the distance in miles:"))
print(f"{mile} = {round(mile*1.609,1)} Kilometer") 
#{round(number you're multiplying * number you're multiplying it by ,numer of decimals to round to)}