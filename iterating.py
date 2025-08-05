# iterating in numpy array -> means going visiting element stap by step using loop

import numpy as np

# iteration in 1D
data1=np.array([1,2,3,4,5])
for ele in data1:
    print(ele)

    # iteration in 2D

data2=np.array([[1,2,3,4],[4,3,2,1]])
for ele in data2:
    print(ele)
data2=np.array([[1,2,3,4],[4,3,2,1]])    
for row in data2:
    for col in row:
        print(col)

        # iteration in 3D
data3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
for i in data3:
    print(i)

for i in data3:
    for j in i:
        for k in j:
            print(k)


# iteration in numpy array using nditer
# now we will iterertate on each scaler

data3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
for ele in np.nditer(data3):
    print(ele)

