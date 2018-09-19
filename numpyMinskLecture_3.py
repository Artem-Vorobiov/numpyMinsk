import numpy as np 

# 						 arithmetic operations

print('\n \t we have 2 arrays \n') 
a = np.array([[1,2],[3,4]])		# Create array
b = np.array([[5,6],[7,8]])		# Create array
print(a, '\n', b, '\n')
c = a + b 						# Calculate

print('\t Result \n')
print(c)

c = 2*(a-b) 					# Calculate
print('\n')
print(c)

#						Mathematics Functions
#					raising to power 
print('\t Raising to power \n')
a = np.reshape(np.arange(6),(2,-1)) 	# Create an array
print(a)
print('\n')

print('\t Raising to 2')
print(np.power(a,2)) 					# Raise to 2
print('\t Raising to a')
print(np.power(a,a)) 					# Raise to a


#					Multiplication
a = np.array([[1,2],[3,4]]) 	# Create
b = np.array([[5,6],[7,8]]) 	# Create
c = np.dot(a,b)

print('\n')
print('\t 	Multiplication \n')
print(c)

#						Indexes and Layers
#						 СРЕЗЫ МАССИВОВ

a = np.arange(8)**2		# Creating an array and then multiply each element on itself
print('\n')
print(a)
print('Choose one element: \t', a[2])

print(a[2:6:2])

# 						multidimensional array
a = np.reshape(np.arange(8),(2,-1))

print('\n')
print(a)
print(a[0,1])
print(a[:,1])
print(a[:,1:3])