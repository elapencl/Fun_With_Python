def vowels1(a):
  count=0
  vowels = ['a','e','i','o','u']
  for i in vowels:
    if i in a:
      count += 1
  return count

print(vowels1('aebnmop'))
