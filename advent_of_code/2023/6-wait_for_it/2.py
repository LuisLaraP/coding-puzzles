#! /usr/bin/env python3

import math

with open("input.txt", "r") as input_file:
    lines = [x.strip() for x in input_file]

T = int(lines[0].partition(":")[2].replace(" ", ""))
D = int(lines[1].partition(":")[2].replace(" ", ""))

disc = math.sqrt(T**2 - 4*D)
lower_bound = math.ceil((T - disc) / 2)
if (T*lower_bound - lower_bound**2) == D:
    lower_bound += 1
upper_bound = math.floor((T + disc) / 2)
if (T*upper_bound - upper_bound**2) == D:
    upper_bound -= 1
result = upper_bound - lower_bound + 1
print(result)
