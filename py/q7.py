a = input('Enter the first number : ')
b = input('Enter the second number : ')
c = input('Enter the third number : ')
if(a>b and b>c):
    print('First number is greatest')
elif(b>a and a>c):
    print('Second number is greatest')
else :
    print('Third number is the greatest')