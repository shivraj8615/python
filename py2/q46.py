#Write a program to iterate over a 2D list in different ways.
rows =3
columns= 2
mylist = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
    for j in range(columns):
        mylist[i][j] = '%s,%s'%(i,j)
print(mylist)
