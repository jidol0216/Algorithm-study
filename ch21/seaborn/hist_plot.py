import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)


sns.histplot(data=iris,x="sepal_length",
                
                hue="species",
                kde=True)

plt.title("Iris Dataset")
plt.show()