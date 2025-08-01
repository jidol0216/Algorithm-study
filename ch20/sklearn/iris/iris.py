from sklearn.datasets import load_iris

iris = load_iris()

import pandas as pd

df =pd.DataFrame(data=iris.data , columns=iris.feature_names)

# print(df)
df["target"] =iris.target

target_names= {
    0:iris.target_names[0],
    1:iris.target_names[1],
    2:iris.target_names[2]
}

df["target"] = df["target"].map(target_names)

print(df)


from sklearn.model_selection import train_test_split
iris_data =df[[
    "sepal length (cm)",
     "sepal width (cm)",
     "petal length (cm)",
     "petal width (cm)"
     ]]
iris_label = df["target"]

train_data,test_data,train_label ,test_label= \
train_test_split(iris_data,iris_label,test_size=0.3)

from sklearn import svm
from sklearn import metrics


clf = svm.SVC()
clf.fit(train_data,train_label)


pre= clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label,pre)
print(f"정답률:{ac_score}")