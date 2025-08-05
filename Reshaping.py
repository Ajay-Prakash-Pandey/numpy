# array reshapping -> changing the shape of array

# reshapping 1d two 2d

import numpy as np

shap=np.array(8)
print(shap.shape)
shap=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(shap)
print(shap.shape)

rshap1=shap.reshape(4,3)
print(rshap1)
print(rshap1.shape)
print(rshap1.ndim)

# reshapping 1d two 3d
rshap2=shap.reshape(2,3,2)
print(rshap2)
# print(rshap2.shape)

shap=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(shap.reshape(3,4).base) # means this is vew not copy

shap=np.array([1,2,3,4,5,6,7,8])
shap1=shap.reshape(2,2,-1)
print(shap1)

# flattering the array by converting multidimension array to 1d

shap=np.array([[1,2,3],[3,2,1]])
shap1=shap.reshape(-1)
print(shap1)

# there are alot of built in function  for changing the shape of array in numpy such as rot90,flip,fliplr,they are comes under advance python




