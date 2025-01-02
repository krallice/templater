
class HLMStandardGenerator:
    """
    A generator for creating Heavy-Light-Medium (HLM) workout schedules based on input weights 
    for squats, pulls, and presses. The program calculates weights for heavy, medium, and light 
    variations of each lift, rounds them to a specified value, and generates a weekly training plan.

    Attributes:
        TEMPLATE_NAME (str): The name of the HLM template.
        ROUNDING_VALUE (float): The value to which calculated weights are rounded.

    Args:
        squat (float): The input weight for squats (default: 100.0).
        pull (float): The input weight for pulls (default: 100.0).
        press (float): The input weight for presses (default: 100.0).
        medium_reduction (float): The reduction percentage for medium intensity (default: 0.10).
        light_reduction (float): The reduction percentage for light intensity (default: 0.20).

    Methods:
        generate(): Prints the workout schedule including input weights and day-by-day exercises.
    """

    TEMPLATE_NAME = "HLM Standard 5s"
    ROUNDING_VALUE = 2.5

    def __init__(self, 
        squat: float = 100.0, 
        pull: float = 100.0, 
        press: float = 100.0,
        medium_reduction: float = 0.10,
        light_reduction: float = 0.20
        ):

        self.weights = {
            "squat": squat,
            "pull": pull,
            "press": press,
        }

        self.reductions = {
            "medium": medium_reduction,
            "light": light_reduction,
        }

        self.calculated_weights = {
            "heavy_squat": squat,
            "medium_squat": self.weights["squat"] * (1 - self.reductions["medium"]),
            "light_squat": self.weights["squat"] * (1 - self.reductions["light"]),
            "heavy_pull": pull,
            "medium_pull": self.weights["pull"] * (1 - self.reductions["medium"]),
            "light_pull": self.weights["pull"] * (1 - self.reductions["light"]),
            "heavy_press": press,
            "medium_press": self.weights["press"] * (1 - self.reductions["medium"]),
            "light_press": self.weights["press"] * (1 - self.reductions["light"]),
        }

        for key in self.calculated_weights:
            self.calculated_weights[key] = round(self.calculated_weights[key] / self.ROUNDING_VALUE) * self.ROUNDING_VALUE

        self.schedule = {
            "Mon": [
                f"Heavy Squat 1x1-5 - {self.calculated_weights['heavy_squat']} kg, 4x5 Backoff",
                f"Medium Press 4x5 - {self.calculated_weights['medium_press']} kg",
                f"Light Pull 3x3-5 - {self.calculated_weights['light_pull']} kg"
            ],
            "Wed": [
                f"Light Squat 3x5 - {self.calculated_weights['light_squat']} kg",
                f"Light Press 3x5 - {self.calculated_weights['light_press']} kg",
                f"Heavy Pull 2x1-5 - {self.calculated_weights['heavy_pull']} kg"
            ],
            "Fri": [
                f"Medium Squat 4x5 - {self.calculated_weights['medium_squat']} kg",
                f"Heavy Press 1x1-5 - {self.calculated_weights['heavy_press']} kg, 4x5 Backoff",
                f"Medium Pull 3x4-5 - {self.calculated_weights['medium_pull']} kg"
            ]
        }

    def generate(self):

        # Generate the output
        output = ""
        output += f"HLM: {self.TEMPLATE_NAME}\n\n"

        # Print the Input Weights:
        output += "Weights:\n"
        for exercise, weight in self.weights.items():
            output += f"  {exercise.title()} (5s) - {weight} kg\n"
        output += "\n"

        for day, exercises in self.schedule.items():
            output += f"{day}:\n"
            for exercise in exercises:
                output += f"  {exercise}\n"
            output += "\n"
        output = output.rstrip("\n")
        output += "\n"

        # Print the workout schedule
        print(output)

class HLMOHPFocusGenerator:
    """
    A generator for creating Heavy-Light-Medium (HLM) workout schedules based on input weights 
    for squats, pulls, and presses. The program calculates weights for heavy, medium, and light 
    variations of each lift, rounds them to a specified value, and generates a weekly training plan.

    Attributes:
        TEMPLATE_NAME (str): The name of the HLM template.
        ROUNDING_VALUE (float): The value to which calculated weights are rounded.

    Args:
        squat (float): The input weight for squats (default: 100.0).
        pull (float): The input weight for pulls (default: 100.0).
        press (float): The input weight for presses (default: 100.0).
        medium_reduction (float): The reduction percentage for medium intensity (default: 0.10).
        light_reduction (float): The reduction percentage for light intensity (default: 0.20).

    Methods:
        generate(): Prints the workout schedule including input weights and day-by-day exercises.
    """

    TEMPLATE_NAME = "HLM Standard 5s (OHP Focus)"
    ROUNDING_VALUE = 2.5

    def __init__(self, 
        squat: float = 100.0, 
        pull: float = 100.0, 
        press: float = 100.0,
        medium_reduction: float = 0.10,
        light_reduction: float = 0.20
        ):

        self.weights = {
            "squat": squat,
            "pull": pull,
            "press": press,
        }

        self.reductions = {
            "medium": medium_reduction,
            "light": light_reduction,
        }

        self.calculated_weights = {
            "heavy_squat": squat,
            "medium_squat": self.weights["squat"] * (1 - self.reductions["medium"]),
            "light_squat": self.weights["squat"] * (1 - self.reductions["light"]),
            "heavy_pull": pull,
            "medium_pull": self.weights["pull"] * (1 - self.reductions["medium"]),
            "light_pull": self.weights["pull"] * (1 - self.reductions["light"]),
            "heavy_press": press,
            "medium_press": self.weights["press"] * (1 - self.reductions["medium"]),
            "light_press": self.weights["press"] * (1 - self.reductions["light"]),
        }

        for key in self.calculated_weights:
            self.calculated_weights[key] = round(self.calculated_weights[key] / self.ROUNDING_VALUE) * self.ROUNDING_VALUE

        self.schedule = {
            "Mon": [
                f"Heavy Squat 1x1-5 - {self.calculated_weights['heavy_squat']} kg, 4x5 Backoff",
                f"Medium Press 4x5 - {self.calculated_weights['medium_press']} kg",
                f"Light Pull 3x3-5 - {self.calculated_weights['light_pull']} kg"
            ],
            "Wed": [
                f"Light Squat 3x5 - {self.calculated_weights['light_squat']} kg",
                f"Heavy Weighted Dips 5x5",
                f"Heavy Pull 2x1-5 - {self.calculated_weights['heavy_pull']} kg"
            ],
            "Fri": [
                f"Medium Squat 4x5 - {self.calculated_weights['medium_squat']} kg",
                f"Heavy Press 1x1-5 - {self.calculated_weights['heavy_press']} kg, 4x5 Backoff",
                f"Medium Pull 3x4-5 - {self.calculated_weights['medium_pull']} kg"
            ]
        }

    def generate(self):

        # Generate the output
        output = ""
        output += f"HLM: {self.TEMPLATE_NAME}\n\n"

        # Print the Input Weights:
        output += "Weights:\n"
        for exercise, weight in self.weights.items():
            output += f"  {exercise.title()} (5s) - {weight} kg\n"
        output += "\n"

        for day, exercises in self.schedule.items():
            output += f"{day}:\n"
            for exercise in exercises:
                output += f"  {exercise}\n"
            output += "\n"
        output = output.rstrip("\n")
        output += "\n"

        # Print the workout schedule
        print(output)
