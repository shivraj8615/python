#  Write a program to find the factorial of a number.
num = int(input('Enter a number : '))
factorial = 1

if(num<0):
    print('Factorial does not exist for negative number')
elif(num==0):
    print('Factorial is 1')
else:
    for i in range(1,num+1):
        factorial = factorial*i
print('The factorial of these number is ',factorial)
    