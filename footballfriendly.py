# Football Friendly
# Create a program that will generate a football friendly matchup between two random teams. Both the selected teams should be different.

# football_teams='Belgium','Brazil','Argentina','England','Germany','Spain','France','Portugal'
# Output Example
# · Brazil vs Argentina

# Hint
# Use an If statement to prevent the same teams from being selected.

import random

football_teams=['Belgium','Brazil','Argentina','England','Germany','Spain','France','Portugal']
team1=random.choice(football_teams)
team2=random.choice(football_teams)

if team1 == team2:
    team2 =  random.choice (football_teams)
    print("The teams that will be playing against each other are: ")
else: 
    print("The teams that will be playing against each other are: ")

print(f"{team1} vs {team2}")
print("LET THE GAMES BEGIN!!!!")