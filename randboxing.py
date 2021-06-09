# Olympic Boxing Matches
# Below is a list containing 8 Female Olympic Boxers.

# olympic_boxers = ['Mary Kom','Nicola Adams','Claressa Sheilds',
# 'Marlen Esparza','Natasha Jonas','Ren Cancan',
# 'Savannah Marshall','Mary Spencer']
# Create a Round of 4 Random Matches between the Boxers. An example has been provided below.

# Output Example
# Summer Olympics - Boxing

# Mary Kom vs Ren Cancan
# Nicola Adams vs Claressa Sheilds
# Natasha Jonas vs Marlen Esparza
# Mary Spencer vs Savannah Marshall

# Things to consider
# The boxer names should not be repeated.
# All 8 boxers should have a Match.
# Hint
# Creating a Copy of the List can greatly help in writing your program

import random 

olympic_boxers = ['Mary Kom','Nicola Adams','Claressa Sheilds', 
'Marlen Esparza','Natasha Jonas','Ren Cancan',
'Savannah Marshall','Mary Spencer']

matches=[]
oc=olympic_boxers.copy() 

for i in range(4):
    boxer1=random.choice(oc)
    oc.remove(boxer1)


    boxer2=random.choice(oc)
    oc.remove(boxer2)
    
    matches.append(f'{boxer1} vs {boxer2}')

print('_'*30)
print('Summer Olympics - Boxing')
print('_'*30)

for i in matches:
    print(i)