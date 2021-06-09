import random

olympic_boxers = ['Mary Kom','Nicola Adams','Claressa Sheilds',
'Marlen Esparza','Natasha Jonas','Ren Cancan',
'Savannah Marshall','Mary Spencer']

olympic_boxers_copy = olympic_boxers.copy()

matches=[]

if len(olympic_boxers) % 2 != 0:
    print("Sorry, you need to have an Even Number of Boxers to schedule the Matchups")
else:
    for x in range(4):
        boxer1 = random.choice(olympic_boxers_copy)
        olympic_boxers_copy.remove(boxer1)
        boxer2 = random.choice(olympic_boxers_copy)
        olympic_boxers_copy.remove(boxer2)
        matches.append(f'{boxer1} Vs {boxer2}')

  

for i in matches:
    print(i)  

 
#    Below is a list named number_range containing a list of numbers from 25 to 50.

# number_range = list(range(25,50))
# Steps
# Locate the Prime numbers from the list
# Store them in a separate list
# Print the Prime Numbers
