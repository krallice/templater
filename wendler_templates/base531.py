from .template import WendlerTemplate

class Base531(WendlerTemplate):

    def __init__(self, bench_onerm, squat_onerm, ohp_onerm, deadlift_onerm):
        self.bench_onerm = bench_onerm
        self.squat_onerm = squat_onerm
        self.ohp_onerm = ohp_onerm
        self.deadlift_onerm = deadlift_onerm
        self.training_maxes = {
            "bench": bench_onerm * 0.9,
            "squat": squat_onerm * 0.9,
            "ohp": ohp_onerm * 0.9,
            "deadlift": deadlift_onerm * 0.9
        }
    
    def generate_plan(self):
        # Define the percentages for each week
        week_percentages = {
            "Week 1 (5/5/5+)": [0.65, 0.75, 0.85],
            "Week 2 (3/3/3+)": [0.70, 0.80, 0.90],
            "Week 3 (5/3/1+)": [0.75, 0.85, 0.95],
            "Week 4 (Deload)": [0.40, 0.50, 0.60]
        }

        # Print the plan
        for week, percentages in week_percentages.items():
            print(f"\n{week}:")
            for lift, tm in self.training_maxes.items():
                print(f"  {lift.capitalize()}:")
                for i, percent in enumerate(percentages):
                    reps = [5, 3, 1][i] if week != "Week 4 (Deload)" else 5
                    weight = tm * percent
                    print(f"    Set {i+1}: {reps} reps @ {weight:.2f} kgs ({percent*100:.0f}%)")