import statsmodels.api as sm


data  = sm.datasets.get_rdataset("mtcars").data

# print(data.head())

x = data['hp']
y = data['mpg']

X =sm.add_constant(x)

model = sm.OLS(y,X).fit()

print(model.summary())