#Write a program to perform spilt and join operation on a list.
result1 = slice(3)
print(result1)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))
py_string = 'AlexSir'
slice_object = slice(3) 
print(py_string[slice_object])
slice_object = slice(1, 6, 2)
print(py_string[slice_object])
pystring = 'Python'
slice_object = slice(-1, -4, -1)
print(pystring[slice_object])
mary = 'Mary had a little lamb'
mary.split()
mwords = mary.split() 
print(mwords)
print(mary.join(mwords))