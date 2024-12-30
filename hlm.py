#!/usr/bin/python3

from libhlm import HLMStandardGenerator

if __name__ == '__main__':
    hlm = HLMStandardGenerator(
        squat=120, 
        pull=140, 
        press=60,
        medium_reduction=0.10, 
        light_reduction=0.20
    )
    hlm.generate()