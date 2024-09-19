import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameimages = [rock, paper, scissors]

userchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if userchoice >= 3 or userchoice < 0:
  print("You picked an invalid number, you lose.")
else:
  print(f"You Selected {userchoice}:" + gameimages[userchoice])
  randomcomputerpick = int(random.randint(0,2))
  print(f"The Computer Selected {randomcomputerpick}:" + gameimages[randomcomputerpick])
  
  if userchoice == randomcomputerpick:
    print("The Game is a Tie.")
  elif userchoice == 0 and randomcomputerpick== 2:
    print("You Win!")
  elif randomcomputerpick == 2 and userchoice == 0:
    print("You Lose")
  
  elif randomcomputerpick > userchoice:
    print("You Lose")
  elif userchoice > randomcomputerpick:
    print("You Win!")