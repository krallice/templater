#!/usr/bin/python3

from libhlm import HLMStandardGenerator, HLMOHPFocusGenerator

if __name__ == '__main__':
    hlm = HLMOHPFocusGenerator(
        squat=140, 
        pull=160, 
        press=75,
        medium_reduction=0.10, 
        light_reduction=0.20
    )
    hlm.generate()