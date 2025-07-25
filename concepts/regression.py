import pandas as pd
import statsmodels.api as sm

df = pd.read_sql("SELECT price, quantity, (price * quantity) AS total_cost FROM Products", conn)
X = df[['price', 'quantity']]
X = sm.add_constant(X)
y = df['total_cost']

model = sm.OLS(y, X).fit()
print(model.summary())