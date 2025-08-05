import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)


sns.boxplot(data=iris,x="species",
            y = "sepal_length"        
        )

plt.title("Iris Dataset")
plt.show()