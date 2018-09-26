from __future__ import division
import ds_library
import ds_algebra
st = 'Hello World!'

if __name__ == '__main__':
	print(st)
	print('5/2: ' + str(5/2))
	print('5//2: ' + str(5//2))

	A=[[1,2,3], [1,1,1], [2,2,3]]
	print(ds_algebra.get_col(A,1))

	