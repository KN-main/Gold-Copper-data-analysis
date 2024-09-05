import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from tabulate import tabulate


df = pd.read_csv('clean_data.csv')

X = df[['Copper Price', 'Buy Price', 'Global Consumer Price Index', 'Gold Price', 'Inventory']]
y = df['Six Month Demand']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

coefficients = pd.Series(model.coef_, index=X.columns)

results = [
    ["MAE", mae],
    ["RMSE", rmse],
    ["R^2", r2]
]

coefficients_table = [["Feature", "Coefficient"]]
for feature, coef in coefficients.items():
    coefficients_table.append([feature, coef])

print("Model Performance Metrics:")
print(tabulate(results, headers=["Metric", "Value"], tablefmt="pretty"))

print("\nModel Coefficients:")
print(tabulate(coefficients_table, headers="firstrow", tablefmt="pretty"))