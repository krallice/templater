from .template import WendlerTemplate

class Base531(WendlerTemplate):

    TRAINING_MAX_RATE = 0.9

    def __init__(self, supplied_tm_inputs, bench_onerm, squat_onerm, ohp_onerm, deadlift_onerm, variation=None):
        # Validate Supplementary:
        if variation not in (None, "fsl-5x5", "fsl-widowmaker", "fsl-pyramid"):
            raise ValueError("FSL_type must be either 'fsl-5x5', 'fsl-widowmaker', 'fsl-pyramid' or None")
        self.variation = variation

        self.bench_onerm = bench_onerm
        self.squat_onerm = squat_onerm
        self.ohp_onerm = ohp_onerm
        self.deadlift_onerm = deadlift_onerm

        if supplied_tm_inputs:
            self.training_maxes = {
                "Bench": bench_onerm,
                "Squat": squat_onerm,
                "OHP": ohp_onerm,
                "Deadlift": deadlift_onerm
            }
        else:
            self.training_maxes = {
                "Bench": bench_onerm * Base531.TRAINING_MAX_RATE,
                "Squat": squat_onerm * Base531.TRAINING_MAX_RATE,
                "OHP": ohp_onerm * Base531.TRAINING_MAX_RATE,
                "Deadlift": deadlift_onerm * Base531.TRAINING_MAX_RATE
            }
    
    def generate_plan(self):
        # Define the percentages and reps for each week
        week_details = {
            "Week 1 (5/5/5+)": {"percentages": [0.65, 0.75, 0.85], "reps": ["5", "5", "5+"]},
            "Week 2 (3/3/3+)": {"percentages": [0.70, 0.80, 0.90], "reps": ["3", "3", "3+"]},
            "Week 3 (5/3/1+)": {"percentages": [0.75, 0.85, 0.95], "reps": ["5", "3", "1+"]},
            "Week 4 (Deload)": {"percentages": [0.40, 0.50, 0.60], "reps": ["5", "5", "5"]},
        }

        # Print the Plan:
        print(f"Wendler 5/3/1: {self.variation if self.variation else 'Base 5/3/1'}")
        print("\nTraining Maxes:")
        for lift, tm in self.training_maxes.items():
            print(f"  {lift}: {tm:.2f} kgs")

        # Print the plan
        for week, details in week_details.items():
            percentages = details["percentages"]
            reps_scheme = details["reps"]
            print(f"\n{week}:")
            
            for lift, tm in self.training_maxes.items():
                print(f"  {lift}:")
                
                # Standard sets and reps for the week
                for i, (percent, reps) in enumerate(zip(percentages, reps_scheme)):
                    weight = tm * percent
                    print(f"    Set {i+1}: {reps} reps @ {weight:.2f} kgs ({percent*100:.0f}%)")

                # Add FSL sets if FSL_type is set and it's not deload week
                if self.variation and week != "Week 4 (Deload)":
                    fsl_weight = tm * percentages[0]  # First Set Last (FSL) weight
                    if self.variation == "fsl-5x5":
                        print(f"    5x5 FSL: 5 sets of 5 reps @ {fsl_weight:.2f} kgs ({percentages[0]*100:.0f}%)")
                    elif self.variation == "fsl-widowmaker":
                        print(f"    Widowmaker FSL: AMRAP (15-20) @ {fsl_weight:.2f} kgs ({percentages[0]*100:.0f}%)")
                    elif self.variation == "fsl-pyramid":
                        for i, (percent, reps) in enumerate(list(zip(percentages[::-1], reps_scheme[::-1]))[1:]):
                            weight = tm * percent
                            if i == len(reps_scheme) - 2:
                                print(f"    Set {i+4}: {reps}+ reps @ {weight:.2f} kgs ({percentages[1-i]*100:.0f}%)")
                            else:
                                print(f"    Set {i+4}: {reps} reps @ {weight:.2f} kgs ({percentages[1-i]*100:.0f}%)")