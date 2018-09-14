import numpy as np 

# 						 arithmetic operations 
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = a + b

print('\n')
print(c)

c = 2*(a-b)
print('\n')
print(c)

#						Mathematics Functions
#					raising to power 

a = np.reshape(np.arange(6),(2,-1))
print('\n')
print(a)

print(np.power(a,2))
print(np.power(a,a))


#					Multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.dot(a,b)

print('\n')
print(c)

#						Indexes and Layers
a = np.arange(8)**2
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