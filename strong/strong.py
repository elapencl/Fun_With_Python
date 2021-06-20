def strong(n):
  result = 0
  for item in str(n):
    result += factorial(int(item))
  if result == n:
    return True
  else:
    return False

def factorial(n):
  if n ==0:
    return 0
  elif n ==1:
    return 1
  elif n > 0:
    result = n*factorial(n-1)
  return result

print(strong(145))
