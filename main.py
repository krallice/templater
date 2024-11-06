#!/usr/bin/python3

from onerm_calculators import EpleyCalculator, BrzyckiCalculator, LombardiCalculator
from wendler_templates import Base531

if __name__ == '__main__':
    print('Hello, World!')
    plan = Base531(100, 100, 100, 100, "FSL_Pyramid")
    plan.generate_plan()