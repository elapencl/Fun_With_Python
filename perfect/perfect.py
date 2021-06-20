def perfect(n):
  list1 = []
  for item in range(1,n):
    if n%item == 0:
      list1.append(item)
  if sum(list1) == n:
    return True
  else:
    return False

print(perfect(1))
