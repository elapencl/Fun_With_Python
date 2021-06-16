#using Replit

from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

new_list = {}
next_bidder = 'yes'

def who_won(list):
  amount = 0
  for key in new_list:
    if int((new_list['bid'])) > int(amount):
      amount = new_list['bid']
      winner = new_list['name']
  clear()
  print(logo)
  print(f"The winner is {winner}")
  return winner


while next_bidder != 'no':
  clear()
  new_dict = {}
  new_dict['name'] = input("What is your name? ")
  new_dict['bid'] = input("What's your bid? ")
  new_list.update(new_dict)
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
who_won(new_list)
