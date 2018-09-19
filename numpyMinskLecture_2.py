import numpy as np 

#				JOIN according ROW -> vstack()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print('\t 	two first arrays: \n', a)
print(b, '\n')
c = np.vstack((a,b))
print('\t ROW way\n')
print(c)

#				JOIN according COLUMN -> hstack()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
c = np.hstack((a,b))
print('\t COLUMN way \n')
print(c)

#				divide Horizontally -> hsplit()
print('\n','		DIVIDE HORIZONTALLY')
aa = np.floor(10*np.random.random((2,12)))
print(aa)

print('\n')
bb = np.hsplit(aa,3)
print(bb)

#				divide Vertically -> hsplit()
print('\n','		DIVIDE VERTICALLY')
aa = np.floor(10*np.random.random((4,2)))
print(aa)

print('\n')
bb = np.vsplit(aa,2)
print(bb)