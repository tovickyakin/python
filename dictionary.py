shopping={'Milk':34,'Butter':450,'bread':343}
# 


# for i in shopping.keys():
#      print(i)   

# for j in shopping.values():
#     print(j)

shopping['Milk']=54
#This is how to append in dictionary 
#Dictionary does not allow duplicates so it will just update the original item

shopping.pop('Milk')
#.pop is how to remove items in dictionary 

shopping.popitem()
#.popitem will remove the last item in the dictionary by default 

for i,j in shopping.items():
        print(i,j)