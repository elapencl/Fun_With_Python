alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import string


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

numbers_symbols = [0,1,2,3,4,5,6,7,8,9]
alphabet1 = list(string.ascii_lowercase)
alphabet = alphabet1 + alphabet1


def caesar(text, shift, direction):
  caesar_list = []
  if direction == "decode":
    shift = -(shift)
  for i in text:
    if i in alphabet:
      new_index = int(alphabet.index(i))
      caesar_list.append(alphabet[(new_index+int(shift))])
    else:
      caesar_list.append(i)
  print("".join(caesar_list))
  answer = input("Would You Like To Start Again? Type 'yes' or 'no'. ")
  if answer == 'yes':
    text1 = input("Please write some text down. ")
    shift1 = int(input("Write the shift down. "))
    shift1 = shift1%26
    direction1 = input("Would you like code or decode? ")
    caesar(text1, shift1, direction1)
  if answer == 'no':
    print('Thank You!')

print(logo)
text = input("Please write some text down. ")
shift = int(input("Give me a shift. "))
direction = input("Is it decode or encode? ")
shift = shift % 26

caesar(text, shift, direction)
