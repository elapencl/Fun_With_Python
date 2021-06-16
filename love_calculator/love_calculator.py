print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1 + name2).lower()

true_score = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_score = names.count("l") + names.count("o") + names.count("v") + names.count("e")

score = str(true_score) + str(love_score)
print(f"Your total score is {score}!")

if int(score) < 10 or int(score) > 90:
  print("You go together like coke and mentos.") 

elif 40< int(score) <50:
  print("You are alright together.")

else:
  print("You're alright together.")
