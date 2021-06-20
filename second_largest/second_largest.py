#example 1

list2 = []

def second_largest(list1):
  global list2
  list2.append(int(len(list1)))
  n = 0
  for i in list1:
    if i>n:
      n = i
  if (list2[0]-1) == int(len(list1)):
    return n
  else:
    list1.remove(n)
    return second_largest(list1)


a = second_largest([1,9,3,11,7,10])
print(a)

# example 2

def second(list1):
  list1.remove(max(list1))
  return max(list1)

print(second([1,6,11,3,4,10]))
