from .onerm_calculator import OneRepMaxCalculator

class LombardiCalculator(OneRepMaxCalculator):
    @classmethod
    def calculate(self, weight, reps):
        return weight * (reps ** 0.1)