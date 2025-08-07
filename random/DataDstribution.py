# data Distribution ->It is a list of all possible value and how often each value occur.

'''
Random Distribution:Probality function.
Now we will genrate 1-D with 100 values where each value has to be 3,5,7,9.
the probality for the value 3 is set be 0.1
the probality for the value 5 is set be 0.3
the probality for the value 7 is set be 0.6
the probality for the value 9 is set be 0
the sum of all problity number should be 1.
'''

from numpy import random as np

data=np.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=100)
print(data)

# now we will return 2-d with three rows each containing 5 values

data2=np.choice([3,5,7,9],p=[0.1,0.3,0.5,0.1],size=(3,5))
print(data2)