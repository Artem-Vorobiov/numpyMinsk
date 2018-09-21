import numpy as np 
from scipy import linalg

#				Детерминант (определитель)
#				Determinant (indicator)

A = np.mat([[1,3,5],[2,5,1],[2,3,8]])
detA = linalg.det(A)

print('\n \t Determinant: \n', detA)



#				Собственные числа и собственные вектора
#
A 		= np.mat([[1,2],[3,4]])
lamb, v = linalg.eig(A)

print('\n \t Собственные значение: \n', lamb)
print('\n \t Собственные вектора : \n', v) 

#				Interpolation
#				Интерполяция. Функция одной переменной.

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,10,num=11, endpoint=True)
print('\n \t Basic: \n', x)

y = np.cos(-x**2/9.0)
print(y)

# plt.plot(x,y,'o')
# plt.show()


#				Линейная интерполяция

f = interp1d(x,y)
print('\n')
print(f(2.5))

xnew = np.linspace(0,10, num=41, endpoint=True)
plt.plot(x,y,'o', xnew, f(xnew), '-')
plt.legend(['graph', 'liniar interpolation.'], loc = 'best')
plt.show()