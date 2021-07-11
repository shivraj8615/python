#Write a program to create a table of 3*3 square cells in a canvas and to colour each cell differently using tkinter library.
from tkinter import *
root = Tk()
root.geometry('300x300')

c = Canvas(root,height=250,width=300,bg='red')
r1 = c.create_rectangle(20,20,50,50,fill='blue')
r2 = c.create_rectangle(70,20,50,50,fill='red')
r3 = c.create_rectangle(20,70,50,50,fill='green')
r4 = c.create_rectangle(120,20,50,50,fill='snow')
r5 = c.create_rectangle(20,120,50,50,fill='white')
r6 = c.create_rectangle(120,70,50,50,fill='red')
r7 = c.create_rectangle(70,120,50,50,fill='black')
r8 = c.create_rectangle(20,20,50,50,fill='deep sky blue')
r9 = c.create_rectangle(20,20,50,50,fill='yellow')



c.pack()


root.mainloop()