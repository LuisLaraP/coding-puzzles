#! /usr/bin/env python3

import math

with open("input.txt", "r") as input_file:
    lines = [x.strip() for x in input_file]

time = [int(x) for x in lines[0].partition(":")[2].split()]
dist = [int(x) for x in lines[1].partition(":")[2].split()]

result = 1
for T, D in zip(time, dist):
    disc = math.sqrt(T**2 - 4*D)
    lower_bound = math.ceil((T - disc) / 2)
    if (T*lower_bound - lower_bound**2) == D:
        lower_bound += 1
    upper_bound = math.floor((T + disc) / 2)
    if (T*upper_bound - upper_bound**2) == D:
        upper_bound -= 1
    result *= upper_bound - lower_bound + 1

print(result)
