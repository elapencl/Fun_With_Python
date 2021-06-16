def prime_checker(number):
  if number<2:
    return print('Prime')
  else:
    for i in range(2,number):
      if number%i == 0:
        return print('Not Prime')
  return print("Prime")

n = int(input("Check this number: "))
prime_checker(number=n)
