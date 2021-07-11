#Write a program to store marks of “n” students in a class for “m” subjects using OOP.
class Marks () :
    dict1={}
    n=int(input ("Enter the number of students: "))
    m=int(input ("Enter the number of subjects: "))
    for i in range(1,n+1) :
        marks=[]
        print("Enter the marks of",i," student: ", end="")
        for j in range(1,m+1) :
            x=int(input())
            marks.append (x)
        dict1[i]=marks
obj=Marks()
print (obj.dict1)
