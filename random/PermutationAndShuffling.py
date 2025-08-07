# Permutation And Shuffling

'''
Permutation refers to an arrangement of element like[3,2,1] is Permutation of [1,2,3] and vice versa.
the numpy module provides 2 methods: Shuffling() and Permutation().
'''
# shuffle() changes on original array
# Permutation() does not make  chnage on original array

# now we will shuffle elements for below array:

from numpy import random as nr
import numpy as np

data=np.array([1,2,3,4,5])
nr.shuffle(data)
print(data)

# now we will Permutation elements for below array:
data1=np.array([1,2,3,4,5])
pdata=nr.permutation(data1)
print(pdata)