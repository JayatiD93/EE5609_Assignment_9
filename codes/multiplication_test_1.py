import numpy as np

B=np.array([[3,1],[-4,4]])
BT = np.transpose(B)
P= np.array([[1,2,1],[-1,2,0]])
PT = np.transpose(P)
print('PT=',PT)
X= np.matmul(P,PT)
print('P.PT',X)
Y=np.matmul(PT,P)
print('PT.P',Y)
Z= np.matmul(Y,Y)
m1=np.matmul(PT,BT)
m2=np.matmul(Y,m1)
z_inv = np.linalg.inv(Z) 
print('z_inverse',z_inv)