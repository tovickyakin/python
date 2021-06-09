# Divisbility
# Display all numbers between 1 to 50 that are divisible by 7

# How to check divisibility of a number?
# To check for divisibility, any number divided by 7 should have remainder as 0. The '%' symbol is used to find the remainder upon division.

# num1=int(1:50)
# if(num1%7==0):
#     print("{} is divisible by 7".format(num1))
# else:
#     print("{} is not divisible by 7".format(num1))

num1=[]
for x in range(1,51):
    if (x%7==0):
        num1.append(str(x))
print('These are the numbers between 1 and 5 that are divisible by 7:' )
print (','.join(num1))