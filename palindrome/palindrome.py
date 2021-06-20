# example 1

def palindrome(p):
  list2 = []
  list1 = list(p)
  count = int(len(p))-1
  while count >= 0:
    list2.append(list1[count])
    count -= 1
  r = ''.join(list2)
  print(r)
  if r == p:
    return True
  else:
    return False

print(palindrome('nursesrun'))

# example 2

def palindrome2(p):
  r = p[::-1]
  if p == r:
    return True
  else:
    return False

print(palindrome2('aba'))
