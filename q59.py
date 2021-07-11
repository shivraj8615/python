
class Animals:
    c1= 'hair'
    c2= 'heart'
    c3= 'blood'
class Birds (Animals) :
    c4= 'feathers'
    c5= 'beak'
    c6= 'two legs'
class Dogs (Animals) :
    c7= 'four legs'
    c8= 'canines'
    c9= 'Tails'
class Humans (Animals) :
    c10= 'Two hands and Two legs'
    c11= 'Most developed'
    c12= 'variety of organs'

obj1=Animals ()
obj2=Birds ()
obj3=Dogs ()
obj4=Humans ()

print (obj1.c1)
print (obj2.c2)
print (obj2.c4)
print (obj3.c3)
print (obj4.c3)
