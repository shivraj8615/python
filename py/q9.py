M = int(input('Enter your full marks : '))
per = M/500*100
if(per>=90):
    print('Your Grade is A')
elif(per>=80):
    print('Your Grade is B+')
elif(per>=70):
    print('Your Grade is B')
elif(per>=60):
    print('Your Grade is C+')
elif(per>=50):
    print('Your Grade is C')
else:
    print('You got Grade D ')