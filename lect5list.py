l1=[431,32,33,423,12]
for i in l1:
    print(i)
   
   
print('*'*30)

print(len(l1))  
print(max(l1))
print(min(l1))
print(sum(l1))
average=sum(l1)/len(l1)  
print(average)
#l1.append(13)
# .append = add something to the end of a list 
l1.insert(3,100)
#.insert = insert something into a list (give the index, then the thing you want to add)
#l1.extend([22,33,44])
#.extend = add more than one thing to the end of a list
#l1[2]=333
l1.pop()
 #remove the last item in a list 
l1.remove(100) 
#.remove = remove selected item (name of the items)
l2=l1.copy()
#.copy = copy previous lis
print(l2)
l3=['Z','C','K','A']
l3.sort()
#.sort = sort characters in alphabetical order

l3.sort(reverse=True)
#(reverse=True) sort characters in reverse alphabetical order 
print(l3)
x=sorted(l1,reverse=True)
#sorted = sort numbers in acsending order  
#sorted(list to sort,reverse=True) sort numbers in decsending order 
print(x)
l3.remove('Z')
print(l3)