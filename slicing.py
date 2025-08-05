# Slicing array-> means taking element from one given position to another given position

import numpy as np
slice1=np.array([1,2,3,4,5,6,7,8,9])
print(slice1[3:7])
# from point to end
print(slice1[3:])
# from end to point
print(slice1[:7])
# negative indexing
print(slice1[:-1])

# slicing with condtion
print(slice1[0:8:2])


# slicing in 2D array

slice2=np.array([[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]])
print(slice2[0,1:4],slice2[1,0:])
