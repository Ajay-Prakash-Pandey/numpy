# sorting in numpy

#sort()-> the numpy ndarray object has a function which is called sort(),and this will sort a specified array.

import numpy as np
intData=np.array([1,2,3,65,8,5,9,5,1,5])
sortInteger=np.sort(intData)
print(sortInteger)


StringData=np.array(["banana","cherry",'mango','apple'])
sortString=np.sort(StringData)
print(sortString)

boolData=np.array([True,False,True,True,False])
sortbool=np.sort(boolData)
print(sortbool)

# int2d=np.array([[3,2,4],[5,0,1]]) # this is not possible because mno of element en noth row are not same

# if need to add all array sort so we need to join first both array the sort and then spilt 
int2d=np.array([[3,2,7,4],[5,4,8,3]])
sort2dint=np.sort(int2d)
print(sort2dint)
