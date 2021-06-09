print ("THIS IS MY FIRST PYTHON CODE STRING ")
print ("Multiplication Calculator ")
# number is the variable 
#  ( input ) - allows user to enter an answer 
# int = number 


number = int(input("Display multiplication table of? "))
# range always needs you to put the number next to the end number.
#  AKA IF you want it to end at 10 put the range as (1,11)

for n in range (1,13):
    print( number, 'x', n, '=', number*n)

ans = ( input ("Would you like to do division?"))
if ans == "yes": 
    # Do this.
    for n in range (1,13):
     print( number, ' ÷', n, '=', number/n)
    print("thank you for using our multiplication calculator")
elif ans == "no": 
    # Do that. 
    print("thank you for using our multiplication calculator")
else: 
    print("Please enter yes or no.") 
