import numpy as np 
from scipy import linalg

#		matrix inverse Обратная матрица

A  = np.mat([[1,2],[3,4]])
Ai = linalg.inv(A)

print('\n matrix inverse : \n', Ai)
print('\n matrix multiplication  : \n', Ai*A)

#		СЛУ - система линейных уравнений - linear equation 

A = np.mat([[1,3,5],[2,5,1],[2,3,8]])
b = np.mat([[10],[8],[3]])

print('\n main Matrix : \n', A)
print('\n second Matrix : \n', b)

x = linalg.inv(A).dot(b)	#	inverse then multiply
print('\n Multiplication : \n', x)

#		СЛУ - система линейных уравнений - linear equation 
#							SOLVE

A = np.mat([[1,3,5],[2,5,1],[2,3,8]])
b = np.mat([[10],[8],[3]])

y = linalg.solve(A,b)
print('\n Multiplication : \n', y)