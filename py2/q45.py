#Write a program to create a 2D list and a 3D list.
a_list = [[2,3,4],[5,6,7]]
print(a_list[0][0])
l = a_list[0][0]*a_list[1][0]
print(l)
for i in a_list:
    print(i)
b_list = [[2,3,4],[5,6,7],[8,4,1]]
print(int(b_list[0][0][0]))
l = b_list[0][0][0]*b_list[1][0][1]
print(l)
for j in b_list:
    print(j)