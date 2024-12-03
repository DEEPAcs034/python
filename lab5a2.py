import matplotlib.pyplot as plt
age_men=[25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
bins=[10,20,30,40,50,60,70]
plt.hist(age_men,bins=bins,edgecolor='r')
plt.show()