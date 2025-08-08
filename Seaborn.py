# Seaborn 

# we  have alot of libraray for drawing plots etc
# such as matplotlib ,sub part of matplotlib(pyplot) is called seaborn
# seaborn  libray is made up of using matplotlib libraray
# distplot-distribution plot(cur)

# i want 2d

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0,1,2,3,4,5])
plt.show()

# ploting a distplot without the histogram
sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()




