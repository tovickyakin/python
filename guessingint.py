import random
score=0
computer_score=0
for i in range(10):
    print(f"Round{i+1}")

    guess=int(input("Guess a number between 1 - 10:\n"))
    comp=random.randrange(1,6)
    print(f"You chose: {guess}")
    print(f"The computer chose:{comp}")

    if guess == comp:

      print("******YOU ARE THE WINNER!!!!**************")
      score += 1 
    else:
      print("YOU LOSE; TRY AGAIN!!!")
      computer_score += 1
print(f"player score is {score} and compuer score is  {computer_score}")      