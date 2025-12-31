import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class PredictiveModel:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        return score

    def predict(self, X):
        return self.model.predict(X)

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv("../Schreibtisch/__alca-1880.csv")
    X = data[['Leverage', 'Signal Gained Profit %']].values
    y = data['Duration'].values
    model = PredictiveModel()
    score = model.train(X, y)
    print(f"Model accuracy: {score}")
    predictions = model.predict(X[:5])
    print(f"Predictions: {predictions}")