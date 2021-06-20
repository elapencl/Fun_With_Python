# example 1

def reverse(n):
  list2 = []
  list1 = list(str(n))
  count = int(len(list1))-1
  while count >= 0:
    list2.append(list1[count])
    count -= 1
  num = ''.join(list2)
  return num

print(reverse(9843))

# example 2

def reverse2(n):
  return str(n)[::-1]

print(reverse2(8760))
