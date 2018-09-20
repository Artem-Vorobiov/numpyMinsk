#		Linear algebra

#		SCIPY.LINALG

# 		np.mat ==> Операция умножения по правилам матричной алгебры

import numpy as np 

A = np.mat([[1,2],[3,4]])
B = np.mat([[1,2],[3,4]])

print('\n BASIC: \n', 'first', A, '\n', 'second',B)
print('\n Произведение по правилам матричной алгебры \n', A*B)

#		np.array ==> умножение поэлементно

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])

print('\n Произведение по элементно \n', A*B)