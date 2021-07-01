#Write a program to implement the usage of iterators on strings.
iterable_value = 'SMVDU'
iterable_obj = iter(iterable_value)
 
while True:
    try:
 
        
        item = next(iterable_obj)
        print(item)
    except StopIteration:
 
        
        break