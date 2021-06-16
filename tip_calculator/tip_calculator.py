print("Wlecome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, 15? ")
people = input("How many people to split the bill? ")

cost = (int(bill) + ((int(bill) * int(tip))/100))/int(people)

print("Each person should pay: " + str(cost))
