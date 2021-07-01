#Write a program to demonstrate use of dictionary in Python with their inbuilt functions.
mydict ={
    'name':'Alex','age':30,'University': 'SMVDU'
}
mydict2 ={
    'name' :'Sir','age':34,"University" : 'SMVDU'
}
value = mydict['name']
print(value)
mydict['email']='alex@smvdu.ac.in'
del mydict['name']
print(mydict)
print(mydict.pop('age'))
print(mydict.popitem())
mydict_cpy = dict(mydict)
print(mydict_cpy)
mydict.update(mydict2)
print(mydict)