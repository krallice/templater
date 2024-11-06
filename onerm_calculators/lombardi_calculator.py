from .onerm_calculator import OneRepMaxCalculator

class LombardiCalculator(OneRepMaxCalculator):
    def calculate(self, weight, reps):
        return weight * (reps ** 0.1)