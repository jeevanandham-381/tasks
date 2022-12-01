import functools
import itertools
import operator

n=(5,6,7,5,8)
#print(functools.reduce(operator.add,n))
print(tuple(itertools.accumulate(n,lambda x,y: x*y)))