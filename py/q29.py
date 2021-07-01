# Write a program to print the following pattern.
'''   1
   2  3
 4  5  6'''

currentNumber = 1

stop = 2

rows = 3 

for i in range(rows):

    for column in range(1, stop):

        print(currentNumber, end= "")

        currentNumber += 1

    print("")

    stop += 2