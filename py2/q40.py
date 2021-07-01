"""Write a program to make a list in Python and perform following operations on List:
    a) length using len() function
    b) print element at index 0
    c) adding an elements of a list to another list using + operator
    d) appending an element to the list 
    e) negative indexing in list
    f) remove the first occurrence of element a from list
    g) reverse the list
    h) sort list
"""
friend = ["Karan","Love","Kiya","Kelly","Alia"]
print(friend[0])
# printing any element from list
print(friend[1:3:-1])
# printing element upto any num from list
print(friend)
# printing whole list
friend.append("Creed")
print(friend)
# adding new element at last in list
friend.insert(2,"Me")
print(friend)
# adding new element in certain place
friend = ["Karan","Love","Me","Kiya","Kelly","Alia"]
friend.remove("Me")
print(friend)
# removing any element from list
friend.clear()
print(friend)
# clear all element from list
friend = ["Karan","Love","Me","Kiya","Kelly","Alia"]
friend.pop()
print(friend)
# to remove last element from list
print(friend.index("Me"))
# to get its index
friend = ["Karan","Love","Me","Kiya","Kelly","Alia","Me","Me"]
print(friend.count("Me"))
# to get numbers of time element it in the list
luck_num = ["89","78","45","56","73","39"]
luck_num.sort()
print(luck_num)
# to arrange in ascending order
luck_num.reverse()
print(luck_num)
# to reverse the list
