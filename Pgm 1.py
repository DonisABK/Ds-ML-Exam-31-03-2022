import numpy as np
from numpy import random
m,n=3,3
A = np.random.randint(1,10,size=(m,n))
print(A)
B = np.random.randint(1,10,size=(m,n))
print(B)
AT= np.transpose(A)
print("transpose:",AT)
BT= np.transpose(B)
print("transpose of B:", BT)
AAT= np.multiply(A,AT)
print("AAt=",AAT)
BBT=np.multiply(B,BT)
print("BBt=",BBT)
MBBT=np.multiply(2,BBT)
print("2BBt=",MBBT)
Sol=np.subtract(AAT,MBBT)
print("solution of AAt-2BBt=",Sol)





