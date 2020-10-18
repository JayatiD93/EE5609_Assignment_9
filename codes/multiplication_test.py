import numpy as np
C = np.array([[1,1,0],[-4,0,0]])
A= np.array([[1,-1],[2,2],[1,0]])
B= np.array([[3,1],[-4,4]])

Y= np.matmul(C,A)
print('CA=',Y)

if (Y==B).any():
	print('CA=B is satisfied')
else:
	print('Not matched')

