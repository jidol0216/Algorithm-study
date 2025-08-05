import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)


sns.set_theme(style="whitegrid")
sns.lmplot(data=iris,x="sepal_length",
                y="sepal_width",
                hue="species",
                height=6)

plt.title("Iris Dataset")
plt.show()