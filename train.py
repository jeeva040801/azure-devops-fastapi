import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    "area": [600, 800, 1000, 1200, 1500, 1800],
    "price": [3000000, 4000000, 5000000, 6500000, 8000000, 9500000]
}

df = pd.DataFrame(data)

X = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model saved!")
