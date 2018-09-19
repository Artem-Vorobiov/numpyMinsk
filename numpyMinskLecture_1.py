import numpy as np 

#	 			Coping
#	assignment - create new link for object. Without new piece of Memory
a = np.array([[1,2],[3,4]])
print('\n')
print(a)
b = a
b[0,0] = 6
print('\n')
print(a)
print(b is a)

# 	Use copy() --> gives new piece of memory
b = a.copy()
print('\n')
print(a)
print(b)
print(b is a)

#				Changing Dimension
#	reshape change dimension without changing data
print('\n')
print('\n', '\t Changing Dimension')
a = np.arange(6)
print(a)

b = np.reshape(a,(3,2))
print('\t Changed: \n', b)
b[0,0] = 9 

print('\n')
print(a)
print(b)
print(b is a)

#	If we use '-1' that means dimension defined by numpy
q = np.reshape(np.arange(6),(3,-1))
print('\t dimension defined by numpy \n')
print(q)

# 'C' style transformation - linking step according row
print('\t linking step according row \n')
e = np.reshape(q,-1)
print(e)

# 'F' style transformation linking step according column
print('\t linking step according column \n')
f = np.reshape(q,-1,order='F')
print(f)
print('\n')

# 	RAVEL
print('\t change form and link using RAVEL \n')
r1 = np.ravel(q)
print(r1)
r2 = np.ravel(q, order = 'F')
print(r2)
