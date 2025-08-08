# binomal Distribution  also called  discrete dist or binary output
# param -n(number of trials), p is for probality,size(Shape)

from numpy import random as nr
import matplotlib.pyplot as plt
import seaborn as sns

data=nr.binomial(n=10,p=0.5,size=10)
print(data)


sns.distplot(nr.binomial(10,p=0.5,size=1000),kde=False)
plt.show()


# Difference bitween normal and binomail - normal(continous) and binomial(discrete)

sns.distplot(nr.normal(loc=50,scale=5,size=1000),hist=False,label='Normal')
sns.distplot(nr.binomial(n=100,p=0.5,size=1000),hist=False,label='Binomail')
plt.show()


