# Array shape in numpy

# shape of an array-> no fof elements in eah dimensions is the shaphe of an array

# now we will try to get shape of an array

import numpy as np

shape1=np.array([[1,2,3,4],[1,2,3,4]])
print(shape1.shape)

shape2=np.array([[[1,2,3],[4,5,6]],[[6,5,4],[3,2,1]]])
print(shape2.ndim)
print(shape2.shape)

sh3=np.array([1,2,3,4,5],ndmin=5)
print(sh3)
print(sh3.shape)
