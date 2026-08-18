"""
Abstract base class for a model.

Abstraction means defining what something must be able to do, without
saying how it does it. Model says every model must have a train
method and a predict method, but it does not implement them. Any
class that inherits from Model has to provide its own version.
"""

from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, value):
        pass

    def describe(self):
        return f"Model: {self.name}"
