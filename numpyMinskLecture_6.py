import numpy as np 

#		READING array from file
res = np.loadtxt('file1.txt', delimiter = ' ')
print('Reading from file: \n', res)
print('\n')

# 		Using only columns
res = np.loadtxt('file1.txt', usecols=(1,2))
print('Reading from file, but only columns 1 & 2: \n', res)
print('\n')

# 		Skipping some rows
res = np.loadtxt('file1.txt', skiprows = 2)
print('Skip 2 rows: \n', res)
print('\n')

#		WRITING array
x = np.linspace(0, np.pi, 5).reshape((5,1))
print('Check the basic array: \n', x)
print('\n')
table = np.hstack((x, np.sin(x)))
print('Check hstack(): \n', x)
print('\n')
np.savetxt('sin.txt',table, delimiter = ',')

print('\n')
np.savetxt('sin2.txt',table, fmt = '%7.4f', header = '__data start__', footer = '__data end__')