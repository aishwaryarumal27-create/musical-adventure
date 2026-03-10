import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [2, 4, 7, 11, 16, 23, 31, 41, 53, 67]
}
df = pd.DataFrame(data)
X = df[['X']]
y = df['Y']
lr = LinearRegression()
lr.fit(X, y)
y_pred = lr.predict(X)
r2_linear = r2_score(y, y_pred)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
lr_poly = LinearRegression()
lr_poly.fit(X_poly, y)
y_poly_pred = lr_poly.predict(X_poly)
r2_poly = r2_score(y, y_poly_pred)
print("R^2 score with linear feature:", r2_linear)
print("R^2 score with polynomial features:", r2_poly)