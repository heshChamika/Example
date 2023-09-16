import matplotlib.pyplot as plt
fig,axes = plt.subplots(2,3)

import numpy as np
x = np.arange(1,5,0.2)
axes[0][0].plot(x,x*x)
axes[0][0].set_title('squre')
axes[0][1].plot(x,np.sqrt(x))
axes[0][1].set_title('squre root')
axes[0][2].plot(x,np.exp(x))
axes[0][2].set_title('exp')
axes[1][0].plot(x,np.log10(x))
axes[1][0].set_title('log')
axes[1][1].plot(x,2*x+5)
axes[1][1].set_title('linear')
axes[1][2].plot(x,2*x**2-11*x+10)
axes[1][2].set_title('polynomial')
plt.tight_layout()

plt.show()
