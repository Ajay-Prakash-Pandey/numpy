# Numpy Normal(gaussian) distribution
# random.normal() method haave three parameter loc,scale,size
# loc tells high level
# scale tells position like tell hight and scale etc

# we are genrating a random normal distribution of size of 2*3
from numpy import random as nr
import matplotlib.pyplot as plt
import seaborn as sns


data=nr.normal(size=(2,3))
print(data)

# we are genrating a random normal distribution of size of 2*3 with mean 1 and standard deviation of 2:

data1=nr.normal(loc=1,scale=2,size=(2,3))
print(data1)

# visualization of normal distribution

sns.distplot(nr.normal(size=1000),hist=False)
plt.show()

# the curve of a normal dist is also called called well curve