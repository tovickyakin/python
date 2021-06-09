


a=('Tito','chaya',21)
print(a)
#
#Tuples are mutable 
#Lists are immutable 
print(len(a))
b=list(a)
b[1]='Chaya Ravindra'
b[0]='Tito akin'
a=tuple(b)
#a= tuple(b)== how to update in tuple 
print(a)
# import Unpack
#unpacking of the tuplus
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(yellow)



x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)


a=(5,6)
b=(100,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
#x=[1,2,3,4,5,6,7,8,9]
pow=[2**x for x in range(1,11)]
print(pow)
odd=[x for x in range(200)if x%2 == 1]
print(odd)
even =[x for x in range (200)if x%2== 0]
print(even)
