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


#		Linear Equation
#	Находим корни уравнения
from scipy.optimize import root

def func(x):
	return x + 5 * np.cos(x)

sol = root(func, -1)
print('\n ROOT: \n')
print(sol.x, sol.success)

#	Системы нелинейных уравнений
def func2(x):
	f = [x[0]*np.cos(x[1])-4,\
		x[0]*x[1]-x[1]-5]
	return f
sol = root(func2,[1,1])
print('\n FUNC2: \n')
print(sol.x, sol.success)