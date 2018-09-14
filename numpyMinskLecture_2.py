import numpy as np 

#				GLUE according ROW -> vstack()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
c = np.vstack((a,b))
print('\n')
print(c)

#				GLUE according COLUMN -> hstack()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
c = np.hstack((a,b))
print('\n')
print(c)

#				divide Horizontally -> hsplit()
print('\n','		DIVIDE HORIZONTALLY')
aa = np.floor(10*np.random.random((2,12)))
print(aa)

print('\ n')
bb = np.hsplit(aa,3)
print(bb)

#				divide Vertically -> hsplit()
print('\n','		DIVIDE VERTICALLY')
aa = np.floor(10*np.random.random((4,2)))
print(aa)

print('\n')
bb = np.vsplit(aa,2)
print(bb)