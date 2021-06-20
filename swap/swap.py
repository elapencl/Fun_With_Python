def swap(a):
   a[0], a[int(len(a))-1] = a[int(len(a))-1], a[0]
   return a

print(swap(['a','s','r','d','b']))
