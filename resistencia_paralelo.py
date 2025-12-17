# This file is part of the project's source code.
# Copyright (c) 2025 Daniel Monzon.
# Licensed under the MIT License. See the LICENSE file in the repository root.

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 19:21:51 2025

@author: dmonz
"""

# Script to calculate the equivalent parallel resistance

# Input the resistor values
values = input("Please, write the values of the resistors with " 
               "a blank space between them (i.e. 100 220 330): ")

# Convert the values (string) to a list of numbers (int)
R = [int(x) for x in values.split()]

# Verify that there are no zeros or negative values
if any(r <= 0 for r in R):
    raise ValueError("All values must be positive and different from zero")

# Calculate the equivalent resistance
Req = 1 / sum(1 / r for r in R)

# Show the result
print(f"The equivalent resistance is: {Req:.2f} ohms")


