height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(int(weight)/(float(height) ** 2))
print("Your bmi is " + str(bmi))
if bmi < 18.5:
  print("You are underweight.")
elif 18.5<bmi<25:
  print("You are normal weight.")
elif 25<bmi<30:
  print("You're slightly overweight.")
elif 30<bmi<35:
  print("You are obese.")
elif bmi > 35:
  print("You are clinically obese/")
