def common(a,b):
  count = []
  for i in a:
    if i in b:
      count.append(i)
  return count

print(common('ela','edi'))
