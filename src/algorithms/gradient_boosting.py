import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

class GradientBoosting:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3, subsample=1.0):
        self.model = GradientBoostingRegressor(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            max_depth=max_depth,
            subsample=subsample
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

