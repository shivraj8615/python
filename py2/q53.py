#Write a program to implement the usage of iterators on collections.
from collections import namedtuple
from itertools import product
point = namedtuple('Point',['x','y'])
pt = point(1,-4)
pt2 = point(4,6)
prod = product(pt,pt2)
print(list(prod))
