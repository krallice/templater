#!/usr/bin/python3

import argparse

def do_main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Set the weights for the workout schedule.")
    parser.add_argument("--squat", type=float, default=120, help="Weight for Heavy Squat (5s)")
    parser.add_argument("--pull", type=float, default=140, help="Weight for Heavy Pull (5s)")
    parser.add_argument("--press", type=float, default=60, help="Weight for Heavy Press (5s)")

    parser.add_argument("--medium-reduction", type=float, default=10, help="%% reduction for Medium Days")
    parser.add_argument("--light-reduction", type=float, default=20, help="%% reduction for Light Days")
    args = parser.parse_args()

    # Define heavy weights and reduction percentages
    weights = {
        "Heavy Squat (5s)": args.squat if args.squat is not None else 120,
        "Heavy Pull (5s)": args.pull if args.pull is not None else 140,
        "Heavy Press (5s)": args.press if args.press is not None else 60,
    }

    reductions = {
        "Medium Reduction": (args.medium_reduction / 100) if args.medium_reduction is not None else 0.10,
        "Light Reduction": (args.light_reduction / 100) if args.light_reduction is not None else 0.20
    }

    # Calculate reduced weights
    reduced_weights = {
        "Medium Squat": weights["Heavy Squat (5s)"] * (1 - reductions["Medium Reduction"]),
        "Light Squat": weights["Heavy Squat (5s)"] * (1 - reductions["Light Reduction"]),
        "Medium Pull": weights["Heavy Pull (5s)"] * (1 - reductions["Medium Reduction"]),
        "Light Pull": weights["Heavy Pull (5s)"] * (1 - reductions["Light Reduction"]),
        "Medium Press": weights["Heavy Press (5s)"] * (1 - reductions["Medium Reduction"]),
        "Light Press": weights["Heavy Press (5s)"] * (1 - reductions["Light Reduction"]),
    }

    # Round weights to 0.5 kg (or nearest precision as required)
    for key in reduced_weights:
        reduced_weights[key] = round(reduced_weights[key] * 2) / 2

    # Define workout schedule
    schedule = {
        "Mon": [
            f"Heavy Squat 1x1-5, 4x5 Backoff - {weights['Heavy Squat (5s)']} kg",
            f"Medium Press 4x5 - {reduced_weights['Medium Press']} kg",
            f"Light Pull 3x3-5 - {reduced_weights['Light Pull']} kg"
        ],
        "Wed": [
            f"Light Squat 3x5 - {reduced_weights['Light Squat']} kg",
            f"Light Press 3x5 - {reduced_weights['Light Press']} kg",
            f"Heavy Pull 2x1-5 - {weights['Heavy Pull (5s)']} kg"
        ],
        "Fri": [
            f"Medium Squat 4x5 - {reduced_weights['Medium Squat']} kg",
            f"Heavy Press 4x5 - {weights['Heavy Press (5s)']} kg",
            f"Medium Pull 3x4-5 - {reduced_weights['Medium Pull']} kg"
        ]
    }

    # Generate the output
    output = ""

    print("Weights:")
    for exercise, weight in weights.items():
        output += f"  {exercise} - {weight} kg\n"
    output += "\n"

    for day, exercises in schedule.items():
        output += f"{day}:\n"
        for exercise in exercises:
            output += f"  {exercise}\n"
        output += "\n"
    output = output.rstrip("\n")
    output += "\n"

    # Print the workout schedule
    print(output)

if __name__ == "__main__":
    do_main()
