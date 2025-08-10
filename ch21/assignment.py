import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = np.random.normal(loc=50, scale=10, size=1000)

sns.histplot(data, bins=30, kde=True)  
plt.title("Normal Distribution (mean=50, std=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
