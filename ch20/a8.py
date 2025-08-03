from sklearn.linear_model import LogisticRegression


X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


model = LogisticRegression()
model.fit(X, y)

new_data = [[4.5], [6.5]]


predictions = model.predict(new_data)

print("예측 결과:", predictions)
