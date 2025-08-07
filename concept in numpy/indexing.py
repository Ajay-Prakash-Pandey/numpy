#Array indexing is same as accessing array element

# 1 d array 
import numpy as np
array1=np.array([1,2,3,4])

print(array1[0])

# we can get two element for adding them
print(array1[2]+array1[3])

for ele in array1:
    print(ele)

# 2 d array 

array2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Second element in the 1st row",array2d[0][1])

# for row in array2d:
#     for col in array2d:
#         print(array2d[row][col])


array3d=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]],[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]])
print(array3d[1][0][0])

