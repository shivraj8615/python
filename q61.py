class tree :
    def _init _ (self, n, c) :
        self.name = n
        self.colour = c
class fruits (tree) :
    def _init _ (self, n, c) :
        tree. _init _(self, n, c)
    def p(self) :
        print ("The fruit is:", self.name)
        print("The colour is:", self.colour)
class veg (tree) :
    def _init _ (self, n, c) :
        tree. _ init_ (self, n, c)
    def p(self) :
        print ("The vegetable is:", self.name)
        print ("The colour is:", self.colour)
class juice (tree) :
    def _init _ (self, n, f) :
        tree. _init_(self, n, f)
    def p(self) :
        print("The juice is of fruit:", self.colour)
class dry (tree) :
    def _init _ (self, n, c) :
        tree. _init_(self, n, c)
    def p(self) :
        print("The dry fruit is:", self.name)
        print("The colour is:", self.colour)
n = input ("Enter the type of food (Fruit/Vegetable/Juice/Dry Fruit) :")
if n == "Fruit":
    a=input("Enter the name: ")
    b=input("Enter the colour: ")
    f1 =fruits (a, b)
    f1.p()
elif n == "Vegetable" :
    a=input("Enter the name: ")
    b=input("Enter the colour: ")
    v1 =veg (a, b)
    v1.p()
elif n == "Juice" :
    a=input("Enter the fruit it is made of:")
    j1 = juice ("Juice",a)
    j1.p()
elif n == "Dry Fruite" :
    a=input("Enter the name: ")
    b=input("Enter the colour: ")
    d1 =dry (a, b)
    d1.p()
else :
    print ("Invalid Input. ")