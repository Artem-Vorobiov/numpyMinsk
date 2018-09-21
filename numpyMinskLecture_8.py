import numpy as np 

#	Matrix and Column Multiplication
#								FIRST WAY

A = np.mat([[1,2],[3,4]])
b = np.mat([1,2])
c = A*b					# Первый пример не работает из-за этой строчки

print('\n \t Array:', A)
print('\n \t Column:', b)
print('\n \t Matrix and Column Multiplication:', c)

#	ValueError: shapes (2,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)
#	Эта ошибка вызвана не соотвествием размерностей

# 	Транспонированная матрица — матрица. , полученная из исходной матрицы. заменой строк на столбцы.
A = np.mat([[1,2],[3,4]])
b = np.mat([1,2])
c = A*b.T 				#	====>>>>	 После транспонирования все заработало

print('\n \t Array:', A)
print('\n \t Column:', b)
print('\n \t Matrix and Column Multiplication:', c)

#								SECOND WAY

A = np.mat([[1,2],[3,4]])
b = np.mat([[1,2]])
c = A*b

print('\n \t Array:', A)
print('\n \t Column:', b)
print('\n \t Matrix and Column Multiplication:', c)