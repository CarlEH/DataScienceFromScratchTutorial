from functools import reduce
import math

# Vectors
def vector_add(v, w):
    """add two vector"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_substract(v, w):
    """substract two vector"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    """sum all the corresponding elements of the vectors"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum_enhanced(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(vector, k):
    """multiply all the values of a vector by a constant k"""
    return [k * v_i for v_i in vector]

def vectors_mean(vectors):
    """compute the vector whose ith element is the mean of the ith of all input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot_product(v, w):
    """returns v_1*w_1 + ... + v_n*w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(vector):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot_product(vector, vector)

def magnitude(vector):
    """length of a vector"""
    return math.sqrt(sum_of_squares(vector))

def squared_distance(v, w):
    """(v_1 - w_1) **2 + ... + (v_n - w_n) **2"""
    return sum_of_squares(vector_substract(v, w))

def distance(v ,w):
    return math.sqrt(squared_distance(v, w))

# Matrices
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i] if A and len(A) < i else []

def get_col(A , i):
    return [A[n][i] for n in range(len(A))]

def make_matrix(num_row, num_col, input_func):
    """returns a row * col dimension matrix whose (ith, jth) element is input_func(i , j)"""
    return [[input_func(i, j) for j in range(num_col)]
            for i in range(num_row)]


