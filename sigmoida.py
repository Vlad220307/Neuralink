import matplotlib.pylab as plt
import numpy as np 

x = np.arange(-8, 8, 0.1)
sigmoida = 1 / (1  + np.exp(-x))

plt.plot(x, sigmoida)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


