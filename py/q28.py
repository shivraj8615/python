#Write a program to print the following pattern.
'''……….
    321
      32
        3'''
def a(n):
    num=1 
    for i in range (4,n,-1):
        num=3
      
        for j in range (0,i-1):
            
           
            print(num ,end=" ")
            
        
         
            num=num-1
        print("\r")
n=0
a(n)
 