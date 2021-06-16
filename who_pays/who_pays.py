names_string = input("Give me everybody's names, separated by a comma uh and esc. ")
names = names_string.split(", ")

import random

choice = random.randint(0, len(names) - 1)
print(names[choice] + " will pay")
