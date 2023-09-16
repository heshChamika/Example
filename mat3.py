import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi, 100)


y = np.sin(x)


plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)


plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.legend()


plt.show()
