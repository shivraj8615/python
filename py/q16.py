# Write a program to check whether a given number is prime or not.
num = int(input('Enter a number : '))
f = False
for i in range(2,num):
    if(num%i==0):
        f = True
    else:
        f=False
if(f==True):
    print(num,'is  prime number')
else:
    print(num,'is not Prime number')