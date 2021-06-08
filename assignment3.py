# Create a Shopping Cart Application that enables you to Add and Remove as many Items as you want
shopping_list=['eggs','bread','flour','chicken']
print('*'*30)

for i in shopping_list:
    print(i)
print('*'*30)
while True:
    ask=int(input('''WOULD YOU LIKE TO 
    1.Add
    2.Exit
    3.Update:\n'''))
 

#ask=input('DO YOU NEED TO ADD ANYTHING ELSE???')

    if ask==1:
        item=input('WHAT DO YOU NEED TO ADD???:\n')
        shopping_list.append(item)
        print('*'*30)
        print(shopping_list)
        print('TIME TO HEAD TO THE CHECKOUT')
    elif ask==3:
        remove1=input('What things on the list have you already bought?:\n')  
        shopping_list.remove(remove1)
        print(shopping_list)
    else:
         print('TIME TO HEAD TO THE CHECKOUT')
         exit()         

