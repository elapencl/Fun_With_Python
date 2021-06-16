two_digit_number = input("Type a two digit number: ")
sum = 0
for c in map(int, two_digit_number):
  sum = c + sum
print(sum)
