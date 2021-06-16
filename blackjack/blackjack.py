#using replit

import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
      

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

def get_2cards(player_cards):
    player_cards.extend([random.choice(cards), random.choice(cards)])
    return user_cards


def get_1card(player_cards):
    player_cards.append(random.choice(cards))
    return player_cards


def calculate_score(player_cards):
  if sum(player_cards) == 21 and len(player_cards) == 2:
    player_score = 0
    return player_score
  if 11 in player_cards and sum(player_cards) > 21:
    player_cards.remove(11)
    player_cards.append(1)
  
  player_score = sum(player_cards)
  return player_score

def compare_score(user_score, dealer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif user_score == 0:
    return "You won with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
      "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_BlackJack():
  
  clear()
  print(logo)

  user_cards = []
  computer_cards = []
  user_score = 0
  computer_score = 0

  get_2cards(user_cards)
  user_score = calculate_score(user_cards)

  print(f"The cards you got are {user_cards}. Your current score is {user_score}. "
        )

  get_2cards(computer_cards)
  computer_score = calculate_score(computer_cards)

  print(f"The computer's first card is {computer_cards[0]}.")

  if computer_score == 0:
    next_game = input(
                f"The computer won! 😤 It had a BlackJack: {computer_cards}. Would you like to play another round? Type 'y' or 'no'. "
            )
  elif user_score == 0:
    next_game = input(
                f"You won! 😃 You had a BlackJack: {user_cards}. Would you like to play another round? Type 'y' 'no'. "
            )
  elif user_score == computer_score:
    next_round = input(
                "You got same score, draw!  🙃 Type 'y'. ")          
  else:
    next_round = input(
                "Would you like to draw another card? Type 'y' or 'n'. ")

  if next_round == 'y':
    get_1card(user_cards)
    user_score = calculate_score(user_cards)
