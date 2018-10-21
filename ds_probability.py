from __future__ import division
import random as rnd 
import math

def uniform_pdf(x):
    """uniform probability density function"""
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    """return the probability that a uniform
    random variable is less or equal to  x"""
    if x < 0: return 0
    if x < 1: return x
    else: return 1

def normal_pdf(x, mu=0, sigma=1):
    """mu is the median and sigma is the standard deviation ie: sqrt(covariance)"""
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2 /(2 * sigma**2))) / (sqrt_two_pi * sigma)

def normal_cdf(x, mu=0, sigma=1):
    #print('x: ', x, ' mu: ', mu, ' sigma: ', sigma)
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2
   # return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    #if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0 #normal_cdf(-10) is very close to 0
    hi_z = 10 #normal_cdf(10) is very close to 1

    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            #midpoint is too low, search above it
            low_z = mid_z
        elif mid_p > p:
            #midpoint is too high search below it
            hi_z = mid_z
        else:
            break
    return mid_z

def bernouilli_trial(p):
    return 1 if rnd.random() < p else 0

def binomial(n,p):
    return sum(bernouilli_trial(p) for _ in range(n))