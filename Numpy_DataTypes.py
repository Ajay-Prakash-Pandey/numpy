# datatypes in numpy
'''
datatypes are :
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''
# checking tthe datatype of numpy array 
# for checking datatype(dtype) keyword is used 
import numpy as np
data1=np.array([1,2,3,4,5,6,7,8,9])
print(data1.dtype)

# checking tthe datatype of numpy array  Strign
data2=np.array(['apple','banana','guaya'])
print(data2.dtype)

#  converting datatypes
# for this  we use dtype
convertdata=np.array([1,2,3,4,5,6,7,8,9],dtype='S')
print(convertdata)
print(convertdata.dtype)

# creating array with datatype of 4 bit int

bit4=convertdata=np.array([1,2,3,4,5,6,7,8,9],)
print(bit4)
print(bit4.dtype)

# creating dat in existing array - astype()
astypee=np.array([1.1,2,3,4,5,6,7,8,9],dtype='i')
astypee1=astypee.astype('S')
print(astypee)
print(astypee1)
print(astypee.dtype)
print(astypee1.dtype)