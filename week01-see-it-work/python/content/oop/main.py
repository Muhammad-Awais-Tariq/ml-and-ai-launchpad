"""
Entry point for the OOP example.

This connects back to modular programming, base.py and models.py are
separate modules, and main.py imports the classes it needs from them,
the same import pattern used in modular_programming/main.py.

Real world link: this base class plus many child classes pattern
shows up in real ML libraries, for example scikit-learn has a shared
base class that every model (linear regression, decision tree, and so
on) inherits from, each one implementing fit and predict its own way.
"""

from models import MeanModel, LinearModel


def main():
    scores = [70, 85, 90, 60, 75]
    mean_model = MeanModel()
    mean_model.train(scores)
    print(mean_model.describe())
    print("prediction:", mean_model.predict(None))

    points = [(1, 2), (2, 4), (3, 6), (4, 8)]
    linear_model = LinearModel()
    linear_model.train(points)
    print(linear_model.describe())
    print("prediction for x=5:", linear_model.predict(5))

    # both objects share the same interface (train, predict, describe)
    # even though each one works completely differently inside, this
    # shared interface is what abstraction gives us
    for model in (mean_model, linear_model):
        print(model.describe(), "predicts", model.predict(10), "for input 10")


if __name__ == "__main__":
    main()
