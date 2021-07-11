#Write a program to create all shapes in a canvas using tkinter library.
from tkinter import *
root = Tk()
root.geometry('300x300')

c = Canvas(root,height=250,width=300,bg='blue')
l = c.create_line(5,5,200,200,width=5)
o = c.create_oval(20,20,100,100,fill='red')
a = c.create_rectangle(50,50,100,200,fill='red')
#k = c.create_rectangle(100,100,100,100,fill='red')

c.pack()


root.mainloop()