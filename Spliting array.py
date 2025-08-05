# Spliting array in numpy -> braking array into sub array

import numpy as np

# split the array in 3 parts

data1=np.array([1,2,3,4,5,6])
output1=np.array_split(data1,3)
print(output1)

# split the array in 4 parts

output2=np.array_split(data1,5)
print(output2)


# spliting into array with index 

output3=np.array_split(data1,3)
print(output3[0])
print(output3[1])
print(output3[2])

# spliting into 2-d array
data2=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
output4=np.array_split(data2,3)
print(output4)


# split the 2-d into three

data3=np.array([[1,2,9],[3,4,8],[5,6,7],[7,8,6],[9,10,5],[11,12,4]])
output5=np.array_split(data3,3)
print(output5)
