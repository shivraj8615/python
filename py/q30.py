#Write a program to print the following pattern.
'''      1
     2  3
 4  5  6
     7  8'''
def halfDiamondStar(N):
      
    for i in range(N):
  
        for j in range(1, i + 1):
            print(j, end = "")
        print()
   
     
    for i in range(1, N):
  
        for j in range(i, N):
            print(j, end = "")
        print()
N = 5; 
halfDiamondStar(N);
  