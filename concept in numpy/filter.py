# filter in numpy->
'''
getting some element out of an existing array and creating a new array is called filtering 

Crating an array from the element on index 0 to 2:
'''
import numpy as np
intdata=np.array([41,42,43,44])
booldata=np.array([True,False,True,False])
TrIN=intdata[booldata]
print(TrIN)

 #now we will creatye filter array
 #that will return only values highdr than 42

data1=np.array([42,43,41,44,24,25,44,35,39,51,41])
emdata=[]
for ele in data1:
    if ele > 41:
        emdata.append(True)
    else:
        emdata.append(False)
fdata=data1[emdata]
print(emdata)
print(fdata)

# create a filter array that will return only even element from the original array

number=np.array([1,2,3,4,5,6,7,8,9])
evenNo=[]
oddNo=[]
for no in number:
    if no%2==0:
        evenNo.append(True)
        oddNo.append(False)
    else:
        evenNo.append(False)
        oddNo.append(True)
even=number[evenNo]
print(evenNo)
print(even)
odd=number[oddNo]
print(oddNo)
print(odd)

# yes, also create  array filter directly from array

 #that will return only values highdr than 42
data3=np.array([41,42,43,44,45])
empty=data3>42
greter42=data3[empty]
print(greter42)

        