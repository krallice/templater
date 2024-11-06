from .onerm_calculator import OneRepMaxCalculator

class EpleyCalculator(OneRepMaxCalculator):
    def calculate(self, weight, reps):
        return weight * (1 + reps / 30)