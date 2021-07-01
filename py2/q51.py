myset ={1,2,3}
print(myset)
myset.add(2)
print(myset)
myset.discard(3)
print(myset)
myset1 ={1,2,3,4,5}
myset1.clear()
print(myset1)
print(myset.pop())
myset2 ={1,2,3,4,5}
u = myset2.union(myset)
print(u)
diff = myset1.difference(myset2)