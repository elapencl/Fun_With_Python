def armstrong(n):
  result = 0
  for item in str(n):
    result += (int(item)**3)
  if result == n:
    return True
  else:
    return False

print(armstrong(371))
