"""
Two simple models that inherit from the abstract Model class in base.py.

Inheritance lets each class reuse the __init__ method and the
describe method already written in Model, while providing its own
version of train and predict. This avoids writing the same setup code
twice.
"""

from base import Model


class MeanModel(Model):
    """Predicts the average of the training data for every input."""

    def __init__(self):
        super().__init__(name="Mean Model")
        self.mean_value = 0

    def train(self, data):
        self.mean_value = sum(data) / len(data)

    def predict(self, value):
        return self.mean_value


class LinearModel(Model):
    """Predicts using a simple line: y = slope * x + intercept."""

    def __init__(self):
        super().__init__(name="Linear Model")
        self.slope = 0
        self.intercept = 0

    def train(self, data):
        # data is a list of (x, y) pairs
        x_values = [point[0] for point in data]
        y_values = [point[1] for point in data]

        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len(y_values)

        numerator = sum((x - x_mean) * (y - y_mean) for x, y in data)
        denominator = sum((x - x_mean) ** 2 for x in x_values)

        self.slope = numerator / denominator if denominator != 0 else 0
        self.intercept = y_mean - self.slope * x_mean

    def predict(self, value):
        return self.slope * value + self.intercept
