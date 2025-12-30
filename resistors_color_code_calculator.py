# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 17:21:08 2025

@author: dmonz
"""

# This file is part of the project's source code.
# Copyright (c) 2025 Daniel Monzon.
# Licensed under the MIT License. See the LICENSE file in the repository root.

# RESISTOR COLOR CODE CALCULATOR, VERSION #1
# Description: This Python script allows you to obtain automatically
#              the value of the resistance based in the colors of the
#              resistor's bands. It works for 4-bands resistors.

# When asked, digit:
    # b, for black;
    # br, for brown;
    # r, for red;
    # o, for orange;
    # y, for yellow;
    # gn, for green;
    # bl, for blue;
    # v, for purple;
    # gy, for grey;
    # w, for white;
    # g, for gold;
    # s, for silver.
    

# Create color code dictionary
color_dict = {"b":0,
              "br":1,
              "r":2,
              "o":3,
              "y":4,
              "gn":5,
              "bl":6,
              "v":7,
              "gy":8,
              "w":9,
              "g":"5%",
              "s":"10%",
              }

# Enter colors
colors = input("Enter the four colors of the resistor according with the above abreviations, with a blanck space between them, please: ")

# Split the data
color_split = colors.split()

# Show the result printing in display
print(f"The value of the resistance is the following:\n {color_dict[color_split[0]]}{color_dict[color_split[1]]}x10^{color_dict[color_split[2]]} +/- {color_dict[color_split[3]]} \u03A9")

