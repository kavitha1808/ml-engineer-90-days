import numpy as np

class LinearRegressionGD:

    def __init__(self, learning_rate=0.000000001, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = 0
        self.b = 0

    def predict(self, X):
        return self.w * X + self.b

    def compute_cost(self, X, y):

        n = len(X)
        predictions = self.predict(X)

        cost = (1/n) * np.sum((predictions - y) ** 2)

        return cost

    def fit(self, X, y):

        n = len(X)

        for i in range(self.epochs):

            predictions = self.predict(X)

            dw = (2/n) * np.sum((predictions - y) * X)
            db = (2/n) * np.sum(predictions - y)

            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db

            if i % 100 == 0:
                cost = self.compute_cost(X, y)
                print(f"Epoch {i}, Cost: {cost}")
