from typing import Optional

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

class HLMAlternatePressingGenerator:
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
        primary_press (float): The input weight for the primary press (default: 100.0).
        primary_press_name (str): The name of the primary press (default: "OHP").
        secondary_press (float): The input weight for the secondary press (default: 100.0).
        secondary_press_name (str): The name of the secondary press (default: "Weighted Dips").
        medium_reduction (float): The reduction percentage for medium intensity (default: 0.10).
        light_reduction (float): The reduction percentage for light intensity (default: 0.20).
        header_text (Optional[str]): Additional text to include in the workout schedule (default: None).

    Methods:
        generate(): Prints the workout schedule including input weights and day-by-day exercises.
    """

    TEMPLATE_NAME = "HLM 5s (Alternate Pressing)"
    ROUNDING_VALUE = 2.5

    def __init__(self, 
        squat: float = 100.0, 
        pull: float = 100.0, 
        primary_press: float = 100.0,
        primary_press_name: str = "OHP",
        secondary_press: Optional[float] = None,
        secondary_press_name: Optional[str] = None,
        medium_reduction: float = 0.10,
        light_reduction: float = 0.20,
        header_text: Optional[str] = None,
        ):

        self.primary_press_name = primary_press_name
        self.secondary_press_name = secondary_press_name or None

        self.header_text = header_text

        self.weights = {
            "squat": squat,
            "pull": pull,
            "primary_press": primary_press,
            "secondary_press": secondary_press or None
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
            "heavy_press": primary_press,
            "medium_press": self.weights["primary_press"] * (1 - self.reductions["medium"]),
            "light_press": secondary_press if secondary_press else primary_press * (1 - self.reductions["light"]),
        }

        for key in self.calculated_weights:
            self.calculated_weights[key] = round(self.calculated_weights[key] / self.ROUNDING_VALUE) * self.ROUNDING_VALUE

        self.schedule = {
            "Mon": [
                f"Heavy Squat 1x1-5 - {self.calculated_weights['heavy_squat']} kg, 4x5 Backoff",
                f"Medium {self.primary_press_name} 4x5 - {self.calculated_weights['medium_press']} kg",
                f"Light Pull 3x3-5 - {self.calculated_weights['light_pull']} kg"
            ],
            "Wed": [
                f"Light Squat 3x5 - {self.calculated_weights['light_squat']} kg",
                f"Heavy {self.secondary_press_name} 5x5 - {self.calculated_weights['light_press']} kg" if secondary_press else 
                    f"Light {self.primary_press_name} 3x5 - {self.calculated_weights['light_press']} kg",
                f"Heavy Pull 2x1-5 - {self.calculated_weights['heavy_pull']} kg"
            ],
            "Fri": [
                f"Medium Squat 4x5 - {self.calculated_weights['medium_squat']} kg",
                f"Heavy {self.primary_press_name} 1x1-5 - {self.calculated_weights['heavy_press']} kg, 4x5 Backoff",
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
            # Print the press names:
            if exercise == "primary_press":
                exercise = self.primary_press_name
            elif exercise == "secondary_press":
                if self.secondary_press_name:
                    exercise = self.secondary_press_name
                else:
                    continue
            output += f"  {exercise.title()} (5s) - {weight} kg\n" 

        output += self.header_text if self.header_text else "\n"
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
