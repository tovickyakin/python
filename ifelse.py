n1=int(input("enter a number of your choice:\n"))
if n1>0:
    print("The number is positive !!!!!!!!!!!!!!!")
elif n1< 0:
     print("The number is negative !!!!!!!!!")  
else:
    print("the number is Zero")     

n2=int(input("Enter another number:\n"))
if n2%2 == 0:
    print("The given number is even!!!!!!")
else:
    print("The given number is odd!!!!!!!")

s1="Mrs .Chaya Ravindra"    
print(s1.replace("Mrs ","Miss "))