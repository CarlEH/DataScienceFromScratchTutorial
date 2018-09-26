from __future__ import division
from collections import Counter
import ds_algebra as dsa
import math

def mean(x):
    return sum(x)/len(x)

def median(v):
    """return the middle-most point/value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        #return the value of the middle point
        return sorted_v[midpoint]
    else:
        #return the average of the two middle points
        lo = midpoint - 1
        hi = midpoint

        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    """return the pth-percentile value in x, the value less than which p % of the data lies"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """return a list of the most common values"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """translate x by substracting its mean -> the result has mean 0"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """x has at least 2 elements"""
    n = len(x)
    deviations = de_mean(x)
    return dsa.sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile(x):
    return quantile(x, 0.25) - quantile(x, 0.75)

def covariance(x, y):
    n = len(x)
    return dsa.dot_product(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    
    return 0



    