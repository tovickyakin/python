# Has it happened to you that you want to go out somewhere and can't figure out what to wear?

# Create a Planner that will randomly select your favourite choice of clothes, accessories and footwear from your Wardrobe.

# Allow your creativity to flow!!!


from math import remainder
import random

print("What type of clothing do you need to decide on today?")

# clothes=[]
clothes=input("Do you need: shirts, trousers, accesories, shoes or a full outfit?:\n")

if clothes == 'shirts':
      print("You should wear a", random.choice(['red','black','blue']),"shirt" )
elif clothes == 'trousers':
      print("You should wear ", random.choice(['jeans','sweatpants','shorts','cargo pants']))
elif clothes == 'accesories':
      print("You should accesorise with a ", random.choice(['baguette bag','gold necklace','silver hoops','clay rings']))
elif clothes == 'shoes':
     print("You should wear ", random.choice(['air jordans','airforce 1s','gucci flats','doc martens']))
elif clothes == 'full outfit':
     print(f"You should wear a {random.choice(['red','black','blue'])} shirt with, {random.choice(['jeans','sweatpants','shorts','cargo pants'])}, {random.choice(['baguette bag','gold necklace','silver hoops','clay rings'])} and {random.choice(['air jordans','airforce 1s','gucci flats','doc martens'])}")
     
# else:
#     print("this stock is not available")
