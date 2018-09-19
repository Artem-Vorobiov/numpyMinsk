import numpy as np 

#				INDEXING
print('\t 			INDEXING		\n')
a = np.arange(6)*2
print('Basic array: \t', a, '\n')

#				Compare (matching)
print('Matching:\t', a>4, '\n')

# Using array for extracting
print('Extracting: \t', a[a>4], '\n')


#				MIN, MAX, SUM

print('				MIN, MAX, SUM')

a = np.array([[1,2],[3,4]])
print('Basic array: \n', a, '\n')

#	MINIMUM
print('Minimum: \t\t', a.min(), '\n')
print('Minimum value in column:', a.min(axis = 0), '\n')
print('Minimum value in row: \t', a.min(axis = 1), '\n')

#	MAXUMUM
print('Maximum: \t\t', a.max(), '\n')
print('Maximum value in column:', a.max(axis = 0), '\n')
print('Maximum value in row: \t', a.max(axis = 1), '\n')

#	SUM
print('Sum: \t\t\t', a.sum(), '\n')
print('Sum value in column: \t', a.sum(axis = 0), '\n')
print('Sum value in row: \t', a.sum(axis = 1), '\n')

#	MEAN
print('mean: \t\t\t', a.mean(), '\n')
print('mean value in column:', a.mean(axis = 0), '\n')
print('mean value in row:   ', a.mean(axis = 1), '\n')