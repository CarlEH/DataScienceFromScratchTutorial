from __future__ import division
import random as rnd 
import ds_algebra

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(i **2 for i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) 
        for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.0001):
    return [partial_difference_quotient(f, v, i, h) for i,_ in enumerate(v)]


def step(vector, direction_vector, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_vector for v_i,direction_vector in zip(vector, direction_vector)]

def square_gradient(v):
    return [2 * i for i in v]

def safe(f):
    """return a new function that is the same as f 
    except that return infnity when f produces an error"""

    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


def minimize_fn_batch(target_fn, gradient_fn, theta_0, tolerance=0.00001):
    """use gradient descent to find a theta value that minimizes the target function"""

    steps = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001]

    theta = theta_0
    target_fn = safe(target_fn)
    val = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_theta = min([step(theta, gradient, -step) for step in steps], key=target_fn)
        next_val = target_fn(next_theta)

        if abs(val - next_val) < tolerance:
            return theta
        else:
            theta, val = next_theta, next_val

def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def neagate_all(f):
    """the same when f returns a list of values"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_fn_batch(target_fn, gradient_fn, thata_0, tolerance=0.0001):
    return minimize_fn_batch(negate(target_fn),
            neagate_all(gradient_fn),
            thata_0,
            tolerance)

def in_random_order(data):
    """return the elements in data in ar andom order"""
    indexes = [i for i,_ in enumerate(data)]
    rnd.shuffle(indexes)

    for i in indexes:
        yield data[i]

def minimize_fn_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)
    theta = theta_0 #initial guess
    alpha = alpha_0 #initial step
    min_theta, min_val = None, float('inf')
    iterations_with_no_improvements = 0

    #if we go over 100 iterations without improvements we stop
    while iterations_with_no_improvements < 100:
        val = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)
        if val < min_val:
            #if we find a new minimum we remeber it and go back to original step size
            min_theta, min_val = theta, val
            iterations_with_no_improvements = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvements += 1
            alpha *= 0.9

        #take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = ds_algebra.vector_substract(theta, ds_algebra.scalar_multiply(alpha, gradient_i))

    return min_theta

def maximize_fn_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_fn_stochastic(negate(target_fn),
                                    neagate_all(gradient_fn),
                                    x, y, theta_0, alpha_0)