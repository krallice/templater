#!/usr/bin/python3

import argparse
from onerm_calculators import EpleyCalculator, BrzyckiCalculator, LombardiCalculator
from wendler_templates import Base531

def calculate_1rm(weight, reps, calculator):
    if calculator == "epley":
        return EpleyCalculator.calculate(weight, reps)
    elif calculator == "brzycki":
        return BrzyckiCalculator.calculate(weight, reps)
    elif calculator == "lombardi":
        return LombardiCalculator.calculate(weight, reps)
    else:
        raise ValueError(f"Unknown calculator: {calculator}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate a Jim Wendler 5/3/1 program.")
    
    # Calculate 1RM:
    parser.add_argument("--bench-weight", type=float, help="Weight lifted for bench press (in lbs or kg).")
    parser.add_argument("--bench-reps", type=int, help="Reps completed for bench press.")
    parser.add_argument("--squat-weight", type=float, help="Weight lifted for squat (in lbs or kg).")
    parser.add_argument("--squat-reps", type=int, help="Reps completed for squat.")
    parser.add_argument("--deadlift-weight", type=float, help="Weight lifted for deadlift (in lbs or kg).")
    parser.add_argument("--deadlift-reps", type=int, help="Reps completed for deadlift.")
    parser.add_argument("--ohp-weight", type=float, help="Weight lifted for overhead press (in lbs or kg).")
    parser.add_argument("--ohp-reps", type=int, help="Reps completed for overhead press.")
    parser.add_argument("--calculator", choices=["epley", "brzycki", "lombardi"], default="epley",
                        help="1RM calculation formula to use. Default: epley.")
    
    # Directly supply training max (TM):
    parser.add_argument("--bench-tm", type=float, help="Training max for bench press.")
    parser.add_argument("--squat-tm", type=float, help="Training max for squat.")
    parser.add_argument("--deadlift-tm", type=float, help="Training max for deadlift.")
    parser.add_argument("--ohp-tm", type=float, help="Training max for overhead press.")
    
    # Program generation:
    parser.add_argument("--template", type=str, default="fsl-pyramid",
                        help="""The template to use for the Wendler program.
Options: fsl-pyramid, fsl-5x5, fsl-widowmaker. Default: fsl-pyramid.""")

    args = parser.parse_args()

    # Determine whether user supplied 1RMs or TMs
    supplied_1rm_inputs = any([args.bench_weight, args.squat_weight, args.deadlift_weight, args.ohp_weight])
    supplied_tm_inputs = any([args.bench_tm, args.squat_tm, args.deadlift_tm, args.ohp_tm])

    if supplied_1rm_inputs and supplied_tm_inputs:
        parser.error("You cannot mix and match Training Max and 1RM inputs. Provide either 1RM weights/reps or TMs, not both.")

    if not supplied_1rm_inputs and not supplied_tm_inputs:
        parser.error("Provide either 1RM weights/reps or TMs for all lifts.")

    # Calculate 1RMs if weights and reps are provided
    if supplied_1rm_inputs:
        if None in (args.bench_weight, args.bench_reps, args.squat_weight, args.squat_reps,
                    args.deadlift_weight, args.deadlift_reps, args.ohp_weight, args.ohp_reps):
            parser.error("Provide weights and reps for all lifts to calculate 1RMs.")
        
        bench_tm = calculate_1rm(args.bench_weight, args.bench_reps, args.calculator)
        squat_tm = calculate_1rm(args.squat_weight, args.squat_reps, args.calculator)
        deadlift_tm = calculate_1rm(args.deadlift_weight, args.deadlift_reps, args.calculator)
        ohp_tm = calculate_1rm(args.ohp_weight, args.ohp_reps, args.calculator)
    else:
        # Use supplied TMs
        if None in (args.bench_tm, args.squat_tm, args.deadlift_tm, args.ohp_tm):
            parser.error("Provide Training Maxes for all lifts.")
        
        bench_tm = args.bench_tm
        squat_tm = args.squat_tm
        deadlift_tm = args.deadlift_tm
        ohp_tm = args.ohp_tm

    # Generate the Wendler program
    plan = Base531(supplied_tm_inputs, bench_tm, squat_tm, ohp_tm, deadlift_tm, args.template)
    plan.generate_plan()
