# joining or concatination in numpy

import numpy as np

# joining of 1-d array
d1=np.array([1,2,3])
d2=np.array([4,5,6])

output1=np.concatenate((d1,d2))
print("joining",output1)

# joining of 2-d array along with rows(axis = 1)

d1=np.array([[1,2,3],[4,5,6]])
d2=np.array([[6,5,4],[3,2,1]])

output2=np.concatenate((d1,d2),axis=1)
print("joining of 2-d array along with rows(axis = 1)",output1)

# joining array using stack function

output3=np.stack((d1,d2))
print("joining array using stack function",output3)# this give first data then second data

# joining array using stack function along row
d1=np.array([[1,2,3],[4,5,6]])
d2=np.array([[6,5,4],[3,2,1]])
output4=np.hstack((d1,d2))
print("joining array using stack function along row",output4)
# joining array using stack function along col
output5=np.vstack((d1,d2))
print("joining array using stack function along col",output5)

# joining array using stack function along height
output6=np.dstack((d1,d2))
print("joining array using stack function along height",output6)