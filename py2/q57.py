#Write a program to implement the concept of class and object creation.
class Person:
    
    age = 10

    def greet(self):
        print('Hello')



print(Person.age)
print(Person.greet)
print(Person.__doc__)


class Person:
    
    age = 10

    def greet(self):
        print('Hello')


harry = Person()
print(Person.greet)
print(harry.greet)

harry.greet()