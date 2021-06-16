#using replit

from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mult(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2

result = 0
def calculate():
  print(logo)
  finish = False
  first = int(input("What's the first number? "))
  operations = ['+', '-', '*', '/']
  for i in operations:
    print(i)
    print('\n')

  
  while finish == False:
    operate = input(f"Pick an operation to perform on {first}. ")
    second = int(input("What's the second number? "))
    

    if operate == '+':
      result = add(first, second)
      print(result)
    elif operate == '-':
      result = sub(first, second)
      print(result)
    elif operate == '*':
      result = mult(first,second)
      print(result)
    elif operate == '/':
      result = div(first,second)
      print(result)
    

    answer = input(f"Would you like to continue using {result}? Type 'yes' or 'no' please! ")
    if answer == 'yes':
      first = result
    else:
      finish = True
      clear()
      calculate()

calculate()
