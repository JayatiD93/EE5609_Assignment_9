import numpy as np

c1=int(input('Enter any value='))
c2=int(input('Enter any value='))
a1= (2-c1)/2
b1=(4-c1)/4
a2=-4-(c2/2)
b2=-(c2/4)

C = np.array([[a1,b1,c1],[a2,b2,c2]])
print('C=',C)
A= np.array([[1,-1],[2,2],[1,0]])
B= np.array([[3,1],[-4,4]])

Y= np.matmul(C,A)
print('CA=',Y)

if (Y==B).any():
	print('CA=B is satisfied')
else:
	print('Not matched')

