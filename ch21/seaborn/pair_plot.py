import seaborn as sns

import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(iris,hue="species")

plt.show()