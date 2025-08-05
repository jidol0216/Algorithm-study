import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)


sns.violinplot(data=iris,x="species",
            y = "sepal_length" ,
            inner = "quart"       
        )

plt.title("Iris Dataset")
plt.show()