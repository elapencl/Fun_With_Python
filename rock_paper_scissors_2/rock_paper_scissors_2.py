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
choices = [rock, paper, scissors]
hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(choices[hand])


if hand >= 3 or hand < 0:
  print("Invalid input.")

import random

computer = random.randint(0,2)
print(choices[computer])

if hand == 0 and computer == 2:
  print("You win!")
elif hand == 2 and computer == 0:
  print("You lose!")

elif hand == 2 and computer == 1:
  print("You win!")
elif hand == 1 and computer == 2:
  print("You lose!")


elif hand == 0 and computer == 1:
  print("You lose!")
elif hand == 1 and computer == 0:
  print("You win!")

else:
  print("Draw!")
