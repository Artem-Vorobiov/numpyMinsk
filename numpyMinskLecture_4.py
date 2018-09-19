import numpy as np 

a = np.array([[0,1,2], [10,11,12],[100,101,102],[110,111,112]])
print(a)
print('\n')

#			LOOPS for arrays. Loop through arrays

for row in a:
	print('Element', row)
#			Loop through each element

for i in np.ravel(a):
	print('Element', i)

#			Give index

a = np.arange(6)*2
i = np.array([1,3,5,2])
print(a[i])

i = np.array([[1,3],[5,2]])
print(a[i])

#			ЗАКОНЧИЛ в 20:00