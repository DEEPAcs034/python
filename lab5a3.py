import matplotlib.pyplot as plt
from matplotlib import style
age_men=[25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
bins=[10,20,30,40,50,60,70]
style.use('fivethirtyeight')
plt.hist(age_men,bins=10,edgecolor='y',color='g',rwidth=0.7)
plt.xlabel('Age of people',fontsize=20)
plt.ylabel('Number of people',fontsize=20)
plt.title('age vs number of people',fontsize=20)
plt.show()