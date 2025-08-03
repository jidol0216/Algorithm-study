import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])


plt.plot(x, y, marker='o')
plt.title("Line graph of y = 2x")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.xlim(1, 5)
plt.ylim(2, 10)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 4, 6, 8, 10])
plt.tight_layout()
plt.show()
