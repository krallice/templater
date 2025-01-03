#!/usr/bin/python3

from libhlm import HLMStandardGenerator, HLMAlternatePressingGenerator

if __name__ == '__main__':
    hlm = HLMAlternatePressingGenerator(
        # Squat:
        squat=140,

        # Press:
        primary_press_name="OHP",
        primary_press=75,
        secondary_press_name="Weighted Dips",
        secondary_press=50,

        # Pull:
        pull=160,

        # Core Reductions:
        medium_reduction=0.10, 
        light_reduction=0.20,
        
        # Header Text:
        header_text="""
Accessories:
  2-3x10 Chins
"""
    )
    hlm.generate()