#!/usr/bin/python3

def do_main():
    # Define heavy weights and reduction percentages
    weights = {
        "Heavy Squat (5s)": 120,
        "Heavy Pull (5s)": 140,
        "Heavy Press (5s)": 60,
    }

    reductions = {
        "Medium Reduction": 0.10,  # 10% reduction for Medium Days
        "Light Reduction": 0.20,   # 20% reduction for Light Days
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

    # Round weights to 0.5 kg
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
