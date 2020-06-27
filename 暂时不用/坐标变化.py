import numpy as np
# A=np.array([[1.0,2.0],[2.0,1.0]])
# print(A)
# A[:,0],A[:,1] = A[:,1],-A[:,0]
# print(A)
# A=np.array([[1.0,2.0],[2.0,1.0]])
# A[:,0], A[:,1]= -A[:,1], A[:,0]
# print(A)
#上式会有bug，图片见onedrive

#180°变化
A=np.array([[1.0,2.0,3.0],[2.0,1.0,0.0]])
print(A)
A[:,0], A[:,2]=-A[:,0], -A[:,2]+0.5
print(A)
A[:,0], A[:,2]=-A[:,0], -A[:,2]+0.5
print(A)