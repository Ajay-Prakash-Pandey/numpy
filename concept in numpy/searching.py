# searhing array-> you can search an array for a certain value and return the index that get the match by using where()

import numpy as np

data1=np.array([1,2,3,4,7,4,5,4])
search=np.where(data1==4)
print(search) 

# even no
evenNO=np.where(data1%2!=0)
print(evenNO)

# odd no
oddNo=np.where(data1%2==0)
print(oddNo)

'''Find indices where elements should be inserted to maintain order.

Find the indices into a sorted array a such that, if the corresponding elements in v were inserted before the indices, the order of a would be preserved.

Assuming that a is sorted:'''

# data2=np.where([1,2,3,65,8,5,9,5,1,5])
data2=np.array([9,8,6,5,3,2,1])
sSerch=np.searchsorted(data2,4)
print(sSerch)


rSearch=np.searchsorted(data2,7,side='right')
print(rSearch)

# Search where can inserted multiple item in array

data3=np.array([1,2,3,4,7,8,9])
mInsert=np.searchsorted(data2,[5,6])
print(mInsert)