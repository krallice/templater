from abc import ABC, abstractmethod

class WendlerTemplate(ABC):

    @abstractmethod
    def __init__(self, supplied_tm_inputs, bench_onerm, squat_onerm, ohp_onerm, deadlift_onerm, variation=None):
        pass

    @abstractmethod
    def generate_plan(self):
        pass