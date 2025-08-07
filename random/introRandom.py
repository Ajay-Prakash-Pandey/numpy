# random-> somthing which cannot be prdicted logically.

# Now we will create a random number

from numpy import random as np

dint=np.randint(100)
print(dint)

# Now we will create a random floating number

dfloat=np.rand()
print(dfloat)

# Now we will create a random 1-d Array

darray=np.randint(100,size=(5))
print(darray)

# Now we will create a random 2-d Array with 3 row containing 5 random int from from 0 to 100

array2d=np.randint(100,size=([3,5]))
print(array2d)


#  you can also genrate random no from an array

arrayRandom=np.choice([1,5,3,5,6,7,3,9])
print(arrayRandom)

#  you can also genrate random no from 2-d array

arrayRandom=np.choice([1,5,3,5,6,7,3,9],size=(3,5))
print(arrayRandom)