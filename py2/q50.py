#Write a program to demonstrate use of tuple in Python with their inbuilt functions.
my_tuple = ('Max','28','Boston')
print(type(my_tuple))
print(my_tuple[0])
for i in my_tuple:
    print(i)
if'max'in my_tuple:
    print('Yes')
else:
    print('No')
print(len(my_tuple))
print(my_tuple.count('P'))
print(my_tuple.index('o'))
my_list = list(my_tuple)
print(type(my_list))

