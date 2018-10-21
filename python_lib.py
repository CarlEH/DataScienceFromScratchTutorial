from __future__ import division
import random as rnd
import math
from collections import Counter
from matplotlib import pyplot as plt


import ds_library
import ds_algebra
import ds_probability
import ds_gradient_descent

def normal_pdfs_visualization():
	xs = [x/10.0 for x in range(-50, 50)]
	plt.plot(xs, [ds_probability.normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0-sigma=1')
	plt.plot(xs, [ds_probability.normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0-sigma=2')
	plt.plot(xs, [ds_probability.normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0-sigma=0.5')
	plt.plot(xs, [ds_probability.normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1-sigma=1')
	plt.legend()
	plt.title('Various Normals pdfs')
	plt.show()
	
def normal_cdfs_visualization():
	xs = [x/10.0 for x in range(-50, 50)]
	plt.plot(xs, [ds_probability.normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0-sigma=1')
	plt.plot(xs, [ds_probability.normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0-sigma=2')
	plt.plot(xs, [ds_probability.normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0-sigma=0.5')
	plt.plot(xs, [ds_probability.normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1-sigma=1')
	plt.legend()
	plt.title('Various Normals cdfs')
	plt.show()



def random_kid():
    return rnd.choice(['boy', 'girl'])
def girl_probability():
	both_g = 0
	older_g = 0
	either_g = 0

	for _ in range(10000):
		younger = random_kid()
		older = random_kid()

		if older == 'girl':
			older_g += 1
		if older == 'girl' and younger == 'girl':
			both_g += 1
		if older == 'girl' or younger == 'girl':
			either_g += 1
	print("P(both/older): ", both_g/older_g)
	print("P(both/either): ", both_g/either_g)

def compare_binomial_dist_to_normal_approx(p, n, nb_points):
	data = [ds_probability.binomial(n, p) for _ in range(nb_points)]
	#showing actual binomial samples on bar chart
	histogram = Counter(data)
	plt.bar([x - 0.4 for x in histogram.keys()],
			[v / nb_points for v in histogram.values()],
			0.8, color='0.7')

	mu_px = p * n
	sigma_px = math.sqrt(n*p*(1 - p))

	#line chart that shows the normal approximation of the binomial variable
	xs = range(min(data), max(data)+1)
	ys = [ds_probability.normal_cdf(i+0.5, mu_px, sigma_px) - ds_probability.normal_cdf(i-0.5, mu_px, sigma_px) for i in xs]

	plt.plot(xs, ys)
	plt.title('Binomial Dist vs Normal approximation')
	plt.show()

if __name__ == '__main__':
	# print('5/2: ' + str(5/2))
	# print('5//2: ' + str(5//2))

	# A=[[1,2,3], [1,1,1], [2,2,3]]
	# print(ds_algebra.get_col(A,1))

	# girl_probability()

	#normal_cdfs_visualization()

	# print(ds_probability.inverse_normal_cdf(0.98))

	# compare_binomial_dist_to_normal_approx(0.75, 100, 100000)

	#Gradient Descent example
	#random starting point 
	v = [rnd.randint(-100, 100) for _ in range(3)]
	tolerance = 0.000001

	while True:
		gradient = ds_gradient_descent.square_gradient(v)
		next_v = ds_gradient_descent.step(v, gradient, -0.01)
		if ds_algebra.distance(next_v, v) < tolerance:
			print('final resting point: ', v)
			break

		v = next_v
