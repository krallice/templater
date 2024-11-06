from .onerm_calculator import OneRepMaxCalculator

class BrzyckiCalculator(OneRepMaxCalculator):
    def calculate(self, weight, reps):
        return weight * (36 / (37 - reps))