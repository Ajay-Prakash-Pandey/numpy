# difference bitween copy and view
# copy is creating a new memory location 
# in copy, when we change in data view also change
# view is just referencing to that data 
# in view when we change in data view also change

import numpy as np
data1=np.array([1,2,3,4,5])
data2=data1.copy()
print('printing without change in data2',data1)
print('printing without change in data2',data2)
data2[1]=7
print('printing after change in data2',data1)
print('printing after change in data2',data2)

data3=np.array([1,2,3,4,5])
data4=data3.view()
print('printing without change in data3',data3)
print('printing without change in data4',data4)
data3[1]=7
print('printing after change in data3',data3)
print('printing after change in data4',data4)
