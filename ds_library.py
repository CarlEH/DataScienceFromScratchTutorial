from __future__ import division
import random as rng
from functools import partial
from math import pow

def lazy_range(x):
    """A lazy version of range()"""
    i = 0
    while i < x:
        yield i
        i += 1
def double(x):
    return 2 * x 

def magic(*args, **kwargs):
    print("unnamed args: ", args)
    print("named args: ", kwargs)
    
if __name__ == "__main__":
    xs = [1,2,3,4]
    twice_xs = [double(k) for k in xs]
    double_xs = map(double, xs)
    list_doubller = partial(map, double)
    dd_xs = list_doubller(xs)
    print(xs, twice_xs, [k for k in double_xs],  list(dd_xs))
    magic(1,2,key="word",key2="word2")

