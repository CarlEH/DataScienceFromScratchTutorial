from __future__ import division
import math
import ds_probability
import random as rnd

def normal_approximation_to_binomial(n, p):
    """finds mu & sigma corresponding to a binomial(n, p)"""
    mu = p*n
    sigma = math.sqrt(p * (1 - p) * n)

    return mu, sigma

#notmal_cdf is the probability the variable is below the threshold
def normal_probability_below(x, mu=0, sigma=1):
   return  ds_probability.normal_cdf(x)

#it's above the threshold if it's not below it
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - ds_probability.normal_cdf(lo)

#it's between if it is less than hi but greater than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return ds_probability.normal_cdf(hi, mu, sigma) - ds_probability.normal_cdf(lo, mu, sigma)

#it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return ds_probability.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return ds_probability.inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    
    #upper bound should have tail probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    #lower bound should have tail probabillity below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_values(x, mu=0, sigma=0):
    if x>= mu:
        #if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        #if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

#A/B testing experiment
def estimated_parameters(N, n):
    p = n/N
    sigma = math.sqrt(p * (1-p) / N)
    return p,sigma

def ab_test_statistics(N_a, n_a, N_b, n_b):
    p_a, sigma_a = estimated_parameters(N_a, n_a)
    p_b, sigma_b = estimated_parameters(N_b, n_b)

    return (p_b - p_a)/(math.sqrt(sigma_a **2 + sigma_b **2))

if __name__ == "__main__":
    #for p=0.5
    mu0, sigma0 = normal_approximation_to_binomial(1000, 0.5)
    lo, hi = normal_two_sided_bounds(0.95, mu0, sigma0)
    print(lo,hi)
    #the result of these calculations show that for 1000 flips, if we get heads between 469-531 time, then the hypothesis that the dice is fair is true
    #which shows that if the ypothesis is true, approximatly 19 times out of 20 the test will give the correct result

    #for p=0.55
    mu1, sigma1 = normal_approximation_to_binomial(1000, 0.55)
    #type 2 error is when we fail to reject the null hypothesis which will happen when X is still in our original interval
    type_2_error_probabiity = normal_probability_between(lo,hi,mu1,sigma1)
    power = 1 -type_2_error_probabiity
    print(power)

    print(two_sided_p_values(529.5, mu0, sigma0))

    extreme_value_count = 0
    for _ in range(10000):
        num_heads = sum(1 if rnd.random() < 0.5 else 0
                        for _ in range(1000))
        if num_heads >= 530 or num_heads <= 470:
            extreme_value_count += 1
    print(extreme_value_count/10000)

    z = ab_test_statistics(1000, 500, 1000, 380)
    print('ab testing: ', two_sided_p_values(z))