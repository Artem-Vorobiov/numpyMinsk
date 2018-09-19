import numpy as np 

v = np.array([1.0,2.0])		# Create array 
print(v.ndim)	# array Dimension
print(v.shape)	# rows and columns
print(v.size)	# how many cells

print('\n')
print(v)

#			Quality

a = np.array([[1,2,3],[4,5,6]])
print('\n')
print(a.ndim)	# array Dimension
print(a.shape)	# rows and columns
print(a.size)	# how many cells

#			TYPE

print('\n')
print(v.dtype)	# int32
print(a.dtype)	# float64 

#			Functions for creating arrays

f = np.arange(1,3,0.2)
print('\n')
print(f)
print(f.shape)

#			Create 0's array
print('\n')
z = np.zeros(5)
print(z)
z2 = np.zeros((2,1))
print(z2)

# 			Create 1's array
print('\n')
o = np.ones(5)
print(o)
o2 = np.ones((2,1))
print(o2)

#			FUNCTION net with interval
# 	Кортеж это - Tuple
print('\n', '	FUNCTION net with interval --- Made TUPLE')
print('\n')
q = np.linspace(0.0, 2.0, 4)    # Начало 0, конец 2, всего значений 4
print(q)

w = np.linspace(0.0, 2.0, 4, retstep = True)     # Начало 0, конец 2, всего значений 4 и ШАГ
print(w)

# 			Function depend on index
#	fromfunction(function, shape, **kwargs)
print('n')
a = np.fromfunction(lambda i,j: i == j, (3,3))
print(a)