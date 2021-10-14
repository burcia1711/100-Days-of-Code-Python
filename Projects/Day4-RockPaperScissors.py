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

import random
me = 0
comp = 0
for i in range(3):
  
  compChoice = random.randint(0, 2)
  choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n")

  if choice == 0:
    print(rock)
  elif choice == 1:
    print(paper)
  else:
    print(scissors)
    
  print("Computer chose: ")
  if compChoice == 0:
    print(rock)
  elif compChoice == 1:
    print(paper)
  else:
    print(scissors)

  if choice == compChoice:
    print("Draw")
  else:
    if choice == 0:
      if compChoice == 1:
        print("Computer won!")
        comp = comp + 1
      else:
        print("You won!")
        me = me +1
    elif choice == 1:
      if compChoice == 0:
        print("You won!")
        me = me +1
      else:
        print("Computer won!")
        comp = comp + 1
    else:
      if compChoice == 0:
        print("Computer won!")
        comp = comp + 1
      else:
        print("You won!")
        me = me + 1
print(me)
print(comp)
if me == comp:
  print("Draw!!!")
elif me > comp:
  print("YOU'RE THE WINNER!!!")
else:
  print("COMPUTER IS THE WINNER!!!")
