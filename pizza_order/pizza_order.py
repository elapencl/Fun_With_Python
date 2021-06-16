print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill_size = 0
if size == "S":
  bill_size = 15
  if add_pepperoni == "Y":
    bill_size += 2
elif size == "M":
  bill_size = 20
  if add_pepperoni == "Y":
    bill_size += 3
elif size == "L":
  bill_size = 25
  if add_pepperoni == "Y":
    bill_size += 3


if extra_cheese == "Y":
  bill_size += 1

print(f"Your total bill is {bill_size}!")
