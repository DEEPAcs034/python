import matplotlib.pyplot as plt
exp_vals=[1400,600,300,410,250]
exp_labels=["home rent","food","phone/internet bills","car","other utilities"]
plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%0.1f%%',radius=1.5,explode=[0,0,0,0.2,0.1])
plt.show()