import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)


sns.set_theme(style="whitegrid")
sns.scatterplot(data=iris,x="sepal_length",
                y="sepal_width",
                hue="species",
                style="species")

plt.title("Iris Dataset")
plt.show()