class CSE:
    def_init _(self, a, b) :
        self.sub1 = a
        self.sub2 = b
    def subCSE (self) :
        print ("The first subject is: ", self.sub1)
        print("The second subject is: ", self.sub2)
class ECE:
    def _init _(self, a) :
        self.sub3 = a
    def subECE (self) :
        print("The third subject is: ", self.sub3)
class MATH:
    def _init_(self, a):
        self.sub4 = a
    def subMATH (self) :
        print ("The fourth subject in: ", self.sub4)
class PSC:
    def _init_(self, a) :
        self.sub5 = a
    def subPSC (self) :
        print("The fifth subject is: ", self.sub5)
class Student (CSE, ECE, MATH, PSC) :
    def _init_(self, n, s1, s2, s3, s4, s5) :
        self.name = n
        print("\nThe student is of CSE Dept.\nHis name is: ", self.name)
        CSE._init_(self, s1, s2)
        ECE._init_(self, s3)
        ΜΑΤΗ._init_(self, s4)
        PSC._init_(self, s5)

a = "Data Structure using C"
b = "Programming using Python"
c = "Digital Electronics"
d = "Engineering Mathematics"
e = "Discourse on Human Virtues"
n = input ("Enter the student name: ")
s = Student (n, a, b, c, d, e)
s.subCSE ()
s.subECE ()
