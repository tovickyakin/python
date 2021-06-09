# Vowel Count
# For any given word, count the number of vowels

# Sample Output
# Unbelievable
# The world Unbelievable has 6 vowels

word=input('Enter a word and we will find the number of vowels:\n')
lowerword=word.lower()
constants=0
vowels =0

vowelcount={}
for i in lowerword:


     if i in "aeiou" :
         vowels += 1
     elif i in "bcdfghjklmnpqrstvwxyz":
         constants += 1
# for i,j in vowelcount.items():
    # print(f"{word} has {j,i}") 

print(f"{word} has {constants} constants") 
print(f"{word} has {vowels} vowels")   


