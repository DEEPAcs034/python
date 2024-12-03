import matplotlib.pyplot as plt
exp_vals=[1400,600,300,410,250]
exp_labels=["home rent","food","phone/internet bills","car","other utilities"]
plt.pie(exp_vals,labels=exp_labels,shadow=True)
plt.show()