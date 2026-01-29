#!/usr/bin/python3

from enum import Enum
from typing import List, Optional

class OneRMFormula(Enum):
    TRAININGMAX = "trainingmax"
    EPLEY = "epley"
    BRZYCKI = "bryzcki"

class Template(Enum):
    DEFAULT = "default"
    FSL = "fsl"
    WIDOWMAKER = "widowmaker"
    PYRAMID = "pyradmid"

class MaxType(Enum):
    TRAINING_MAX = "training_max"
    ONERM = "onerm"

class WendlerBasic531Generator:

    # Define default percentages for templates
    TEMPLATE_PERCENTAGES = {
        Template.DEFAULT: 90.0,
        Template.FSL: 90.0,
        Template.WIDOWMAKER: 90.0,
        Template.PYRAMID: 90.0
    }

    STRUCTURE_CORE = [
        {"week": 1, "name": "Week 1 (5/5/5+)", "reps": ["5", "5", "5+"], "percentages": [0.65, 0.75, 0.85]},
        {"week": 2, "name": "Week 2 (3/3/3+)", "reps": ["3", "3", "3+"], "percentages": [0.70, 0.80, 0.90]},
        {"week": 3, "name": "Week 3 (5/3/1+)", "reps": ["5", "3", "1+"], "percentages": [0.75, 0.85, 0.95]},
        {"week": 4, "name": "Week 4 (Deload)", "reps": ["5", "5", "5"], "percentages": [0.40, 0.50, 0.60]}
    ]

    def __init__(self, 
                 squat: float = 100.0, bench: float = 100.0, 
                 deadlift: float = 100.0, press: float  = 100.0,
                 active_lifts: Optional[List[str]] = None,
                 max_type: MaxType = MaxType.TRAINING_MAX,
                 tm_percentage: float = 90.0,
                 header_text:Optional[str] = None,
                 templates: List[Template] = None,
                 fsl_params: Optional[dict] = None):
        """
        Initialize the Wendler 5/3/1 generator.

        Args:
            squat (float): Squat max weight.
            bench (float): Bench press max weight.
            deadlift (float): Deadlift max weight.
            press (float): Overhead press max weight.
            active_lifts (Optional[List[str]]): List of active lifts to include (default: all lifts).
            max_type (MaxType): Type of max calculation (Training Max or One Rep Max).
            tm_percentage (float): Percentage of 1RM to use as training max.
            templates (List[Template]): List of templates to include in the program.
            fsl_params (Optional[dict]): Additional parameters for FSL template.
        """

        self.header_text = header_text

        self.templates = templates if templates else []

        self.active_lifts = active_lifts or ['squat', 'bench', 'deadlift', 'press']

        self.max_type = max_type
        self.tm_percentage = tm_percentage
        # Filter maxes to include only active lifts
        all_maxes = {'squat': squat, 'bench': bench, 'deadlift': deadlift, 'press': press}
        self.maxes = self._calculate_training_maxes(
            {lift: all_maxes[lift] for lift in self.active_lifts}
        )

        # Validate the template combinations:
        self._validate_templates()

        # Assign template specific vars:
        if Template.FSL in self.templates:
            self.fsl_params = self._process_fsl_params(fsl_params)

    def _calculate_training_maxes(self, maxes: dict) -> dict:
        """
        Calculate training maxes based on the provided max_type and training max percentage.

        Args:
            maxes (dict): Input maxes (either TMs or 1RMs).

        Returns:
            dict: Training maxes.
        """
        if self.max_type == MaxType.TRAINING_MAX:
            return maxes
        
        tm_percentage = self.tm_percentage or self._get_template_percentage()

        return {lift: max_value * (tm_percentage / 100) for lift, max_value in maxes.items()}

    def _get_template_percentage(self) -> float:
        """
        Retrieve the default training max percentage based on the selected templates.

        Returns:
            float: Default TM percentage for the selected template(s).
        """
        if not self.templates:
            return 90.0  # Default to 90% if no template is provided

        selected_template = self.templates[0]
        return self.TEMPLATE_PERCENTAGES.get(selected_template, 90.0)

    def _validate_templates(self):
        """
        Validate the template combinations to ensure mutual exclusivity.
        Only one of FSL, Pyramid, or Widowmaker can be selected, or none.

        Raises:
            ValueError: If mutually exclusive templates are selected simultaneously.
        """
        mutually_exclusive_templates = {Template.FSL, Template.WIDOWMAKER, Template.PYRAMID}
        selected_exclusive_templates = [t for t in self.templates if t in mutually_exclusive_templates]
        
        if len(selected_exclusive_templates) > 1:
            template_names = [t.value for t in selected_exclusive_templates]
            raise ValueError(f"Templates {template_names} are mutually exclusive. Only one of FSL, Pyramid, or Widowmaker can be selected, or none.")

    def _process_fsl_params(self, fsl_params: Optional[dict]) -> Optional[dict]:
        """
        Validate and process FSL-specific parameters.

        Args:
            fsl_params (Optional[dict]): The FSL parameters (sets and reps).

        Returns:
            dict: Validated FSL parameters or None.

        Raises:
            ValueError: If FSL parameters are invalid or missing when required.
        """
        if Template.FSL not in self.templates:
            return None

        if not fsl_params:
            raise ValueError("When FSL is selected, fsl_params must be provided.")

        sets = fsl_params.get('sets')
        reps = fsl_params.get('reps')

        if not (3 <= sets <= 8):
            raise ValueError("FSL sets must be between 3 and 8.")
        if not (3 <= reps <= 5):
            raise ValueError("FSL reps must be between 3 and 5.")

        return {'sets': sets, 'reps': reps}

    def _round_weight(self, weight: float) -> float:
        """
        Round the weight to the nearest specified value.

        Args:
            weight (float): The weight to round.

        Returns:
            float: Rounded weight.
        """
        round_value = 2.5
        return round(weight / round_value) * round_value

    def generate(self):
        """
        Print the program info and generate the 5/3/1 program.
        """
        print(f"Wendler 5/3/1: {''.join([template.value for template in self.templates])}")

        print(self.header_text) if self.header_text else None

        print("\nTraining Maxes:")
        for lift, tm in self.maxes.items():
            print(f"  {lift.title()}: {tm:.2f} kgs")

        self._generate_plan_core()

    def _generate_plan_core(self):
        """
        Generate the core 5/3/1 program and print the results.
        """
        for week in self.STRUCTURE_CORE:

            print(f"\n{week['name']}:")

            for lift, training_max in self.maxes.items():

                print(f"  {lift.title()}:")

                for i, (percent, reps) in enumerate(zip(week['percentages'], week['reps'])):
                    weight = self._round_weight(training_max * percent)
                    print(f"    Set {i+1}: {reps} reps @ {self._round_weight(weight):.1f} kg ({percent*100:.0f}%)")

                if Template.FSL in self.templates:
                    if week["week"] != 4:
                        print(f"    FSL: {self.fsl_params['sets']} x {self.fsl_params['reps']} @ {self._round_weight(training_max * week['percentages'][0]):.1f} kg")
                elif Template.WIDOWMAKER in self.templates:
                    if week["week"] != 4:
                        print(f"    WIDOWMAKER: AMRAP @ {self._round_weight(training_max * week['percentages'][0]):.1f} kg")
                elif Template.PYRAMID in self.templates:
                    print(f"    PYRAMID: {week['reps'][1]} reps @ {self._round_weight(training_max * week['percentages'][1]):.1f} kg")
                    print(f"    PYRAMID: {week['reps'][0]}+ reps @ {self._round_weight(training_max * week['percentages'][0]):.1f} kg")

def estimate_1rm(weight: float, reps: int, method: OneRMFormula = "BRZYCKI") -> float:
    """
    Estimate a 1RM (One-Rep Max) based on weight and reps using the specified formula.

    Args:
        weight (float): The weight lifted.
        reps (int): The number of reps completed.
        method (str): The formula to use for estimation ('epley', 'brzycki', etc.).

    Returns:
        float: The estimated 1RM.
    """
    if reps == 1:
        return weight  # If it's a true 1RM, return as is

    if method == OneRMFormula.EPLEY:
        return weight * (1 + reps / 30)
    elif method == OneRMFormula.BRZYCKI:
        return weight * (36 / (37 - reps))
    else:
        raise ValueError(f"Unsupported method: {method}")
