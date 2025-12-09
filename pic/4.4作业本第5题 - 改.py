import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
plt.plot(x, x ** 0.3, label="y=x**0.3")
plt.plot(x, x ** 0.5, label="y=x**0.5", linewidth=4)
plt.plot(x, x, label="y=x")
plt.scatter(x, x ** 2, label="y=x**2")
plt.plot(x, x ** 3, label="y=x**3", linewidth=3)

#y = np.linspace(-1,1,50)
#plt.plot(x, [0]*50,color="black", linewidth=0.2)
#plt.plot([0]*50, y,color="black", linewidth=0.2)
plt.legend(fontsize=12)


plt.savefig("c04.04.5function.pdf",pad_inches=0.01,bbox_inches='tight')
plt.show()