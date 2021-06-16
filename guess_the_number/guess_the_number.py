#using replit

from replit import clear
import random

logo = """

  ________                                    __  .__                                     ___.                 
 /  _____/ __ __   ____   ______ ______     _/  |_|  |__   ____         ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/     \   __\  |  \_/ __ \       /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \       |  | |   Y  \  ___/      |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >      |__| |___|  /\___  >     |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                 \/     \/           \/            \/    \/     \/       
       
        """

number = 0
EASY = 10
HARD = 5

def attempts(difficulty):
  
  global number

  print(f"You have {difficulty} attempts to guess the number! ")

  for i in range(0, difficulty):
    guess = int(input("What number did you guess? "))
    if guess == number:
      print(f"You got it! 😁 The answer was {number}! ")
      break
    elif guess < number:
      print("Your guess was too low.")
      if i == 9 or i == 4:
        print("You out of attempts boo-boo 🧟‍♀️")
        break
      print("Try again.")
    elif guess > number:
      print("Your guess was too high.")
      if i == 9 or i == 4:
        print("You out of attempts boo-boo 🧟‍♀️")
        break
      print("Try again.")
  return 

def play_guess():
  clear()
  print(logo)
  print("Welcome to the Number Guessing Game! 🙃\n I'm thinking of a number between 1 and 100.")

  global number

  number = random.randint(1,101)

  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
  if difficulty_level == 'easy':
    attempts(EASY)
  elif difficulty_level == 'hard':
    attempts(HARD)

play_guess()
