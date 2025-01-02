#!/usr/bin/python3

from libhlm import HLMAlternatePressingGenerator

if __name__ == '__main__':
    hlm = HLMAlternatePressingGenerator(
        squat=140, 
        pull=160, 
        primary_press_name="OHP",
        primary_press=75,
        secondary_press_name="Weighted Dips",
        secondary_press=50,
        medium_reduction=0.10, 
        light_reduction=0.20,
        header_text="""
Accessories:
  2-3x10 Chins
"""
    )
    hlm.generate()