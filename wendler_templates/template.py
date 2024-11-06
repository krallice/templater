class WendlerTemplate:
    def __init__(self, bench_onerm, squat_onerm, ohp_onerm, deadlift_onerm):
        self.bench_onerm = bench_onerm
        self.squat_onerm = squat_onerm
        self.ohp_onerm = ohp_onerm
        self.deadlift_onerm = deadlift_onerm

    def generate_plan(self):
        raise NotImplementedError