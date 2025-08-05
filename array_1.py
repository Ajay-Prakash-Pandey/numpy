#  now we will create numpy ndarray object

import numpy as np
# x=np.array([1,2,3,4,5])
# x=np.array(eval(input("Enter a list: ")))
# print(x)
# print(type(x))

#  we can also take a list,tuple or any array like object with array(),and it will be converted to ndarrry

y=np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
print(y)
print(y.ndim) # this(ndim) function tells dimenson of array 

_5dconver=np.array([1,2,3,4,5],ndmin=5) # ndim=5 means to set dimension 5 
print(f"no of dimension in {_5dconver} is: ",_5dconver.ndim)
__5d=np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]],ndmin=5)

print(f"no of dimension in {__5d} is: ",__5d.ndim)