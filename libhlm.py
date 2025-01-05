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

        # Squats:
        heavy_squat_name (str): The name of the heavy squat exercise (default: "Squat").
        squat (float): The input weight for squats (default: 100.0).

        # Presses:
        primary_press (float): The input weight for the primary press (default: 100.0).
        primary_press_name (str): The name of the primary press exercise (default: "OHP").
        secondary_press (float): The input weight for the secondary press (default: None).
        secondary_press_name (str): The name of the secondary press exercise (default: None).

        # Pulls:
        pull (float): The input weight for pulls (default: 100.0).
        heavy_pull_name (str): The name of the heavy pull exercise (default: "Deadlift").
        medium_pull (float): The input weight for the medium pull (default: None).
        medium_pull_name (str): The name of the medium pull exercise (default: None).
        light_pull (float): The input weight for the light pull (default: None).
        light_pull_name (str): The name of the light pull exercise (default: None).

        # Core Reductions:
        medium_reduction (float): The reduction percentage for medium intensity (default: 0.10).
        light_reduction (float): The reduction percentage for light intensity (default: 0.20).

        # Header Text:
        header_text (str): Additional text to include in the workout schedule (default: None).


    Methods:
        generate(): Prints the workout schedule including input weights and day-by-day exercises.
    """

    TEMPLATE_NAME = "HLM 5s (Alternate Pressing)"
    ROUNDING_VALUE = 2.5

    def __init__(self,
        # Squats:
        heavy_squat_name: str = "Squat",
        squat: float = 100.0, 

        # Presses:
        primary_press: float = 100.0,
        primary_press_name: str = "OHP",
        secondary_press: Optional[float] = None,
        secondary_press_name: Optional[str] = None, 
        
        # Pulls:
        pull: float = 100.0,
        heavy_pull_name: str = "Deadlift",

        medium_pull: Optional[float] = None,
        medium_pull_name: Optional[str] = None,

        light_pull: Optional[float] = None,
        light_pull_name: Optional[str] = None,

        # Core Reductions:
        medium_reduction: float = 0.10,
        light_reduction: float = 0.20,
        
        # Header Text:
        header_text: Optional[str] = None,
        ):

        self.header_text = header_text

        self.exercise_names = {
            "heavy_squat": heavy_squat_name,

            "primary_press": primary_press_name,
            "secondary_press": secondary_press_name or None,
            
            "heavy_pull": heavy_pull_name,
            "medium_pull": medium_pull_name or None,
            "light_pull": light_pull_name or None
        }

        self.weights = {
            "heavy_squat": squat,

            "primary_press": primary_press,
            "secondary_press": secondary_press or None,
            
            "heavy_pull": pull,
            "medium_pull": medium_pull or None,
            "light_pull": light_pull or None
        }

        self.reductions = {
            "medium": medium_reduction,
            "light": light_reduction,
        }

        self.calculated_weights = {

            "heavy_squat": self.weights['heavy_squat'],
            "medium_squat": self.weights["heavy_squat"] * (1 - self.reductions["medium"]),
            "light_squat": self.weights["heavy_squat"] * (1 - self.reductions["light"]),
            
            "heavy_press": self.weights['primary_press'],
            "medium_press": self.weights["primary_press"] * (1 - self.reductions["medium"]),
            "light_press": self.weights['secondary_press'] if self.weights['secondary_press'] else self.weights['primary_press'] * (1 - self.reductions["light"]),

            "heavy_pull": self.weights['heavy_pull'],
            "medium_pull": self.weights['medium_pull'] if self.weights['medium_pull'] else self.weights["heavy_pull"] * (1 - self.reductions["medium"]),
            "light_pull": self.weights['light_pull'] if self.weights['light_pull'] else self.weights["heavy_pull"] * (1 - self.reductions["light"]),
        }

        for key in self.calculated_weights:
            self.calculated_weights[key] = round(self.calculated_weights[key] / self.ROUNDING_VALUE) * self.ROUNDING_VALUE

        self.schedule = {
            "Mon": [
                f"Heavy Squat 1x1-5 - {self.calculated_weights['heavy_squat']} kg, 4x5 Backoff",
                f"Medium {self.exercise_names['primary_press']} 4x5 - {self.calculated_weights['medium_press']} kg",
                f"Light {self.exercise_names['light_pull']} 3x3-5 - {self.calculated_weights['light_pull']} kg" if self.weights['light_pull'] else
                    f"Light {self.exercise_names['heavy_pull']} 3x3-5 - {self.calculated_weights['light_pull']} kg"
            ],
            "Wed": [
                f"Light Squat 3x5 - {self.calculated_weights['light_squat']} kg",
                f"Heavy {self.exercise_names['secondary_press']} 1x5 - {self.calculated_weights['light_press']} kg, 4x5 Backoff" if self.weights['secondary_press'] else 
                    f"Light {self.exercise_names['primary_press']} 3x5 - {self.calculated_weights['light_press']} kg",
                f"Heavy {self.exercise_names['heavy_pull']} 2x1-5 - {self.calculated_weights['heavy_pull']} kg"
            ],
            "Fri": [
                f"Medium Squat 4x5 - {self.calculated_weights['medium_squat']} kg",
                f"Heavy {self.exercise_names['primary_press']} 1x1-5 - {self.calculated_weights['heavy_press']} kg, 4x5 Backoff",
                f"Medium {self.exercise_names['medium_pull']} 3x4-5 - {self.calculated_weights['medium_pull']} kg" if self.weights['medium_pull'] else
                    f"Medium {self.exercise_names['heavy_pull']} 3x4-5 - {self.calculated_weights['medium_pull']} kg"
            ]
        }

    def generate(self):

        # Generate the output
        output = ""
        output += f"HLM: {self.TEMPLATE_NAME}\n\n"

        # Print the Input Weights:
        output += "Weights:\n"
        for exercise, weight in self.weights.items():
            if weight == None:
                continue
            exercise_name = self.exercise_names[exercise]
            output += f"  {exercise_name.title()} (5s) - {weight} kg\n" 

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
