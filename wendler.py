#!/usr/bin/python3

from libwendler import WendlerBasic531Generator, Template, OneRMFormula, estimate_1rm

if __name__ == '__main__':

    method = OneRMFormula.BRZYCKI

    user_lifts = {
        "squat": {"weight": 120, "reps": 5},
        "bench": {"weight": 100, "reps": 5},
        "deadlift": {"weight": 150, "reps": 3},
        "press": {"weight": 60, "reps": 8}
    }
    lifts = {}
    for lift, data in user_lifts.items():
        if method != OneRMFormula.TRAININGMAX:
            lifts[lift] = estimate_1rm(data["weight"], data["reps"], method=method)
        else:
            lifts[lift] = data["weight"]  # Use raw weight as 1RM if estimation is disabled

    plan = WendlerBasic531Generator(
        squat=lifts["squat"], bench=lifts["bench"], 
        deadlift=lifts["deadlift"], press=lifts["press"],
        templates=[Template.FSL], 
        fsl_params={'sets': 3, 'reps': 5},
        header_text="""
Accessory Pairings:
  Squat: Chins
  OHP: Dips
  Deadlift: Rows"""
    )
    plan.generate()