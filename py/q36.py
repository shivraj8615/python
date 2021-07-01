#Write a program to demonstrate the use of local and global variables.
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()