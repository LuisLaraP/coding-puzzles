#! /usr/bin/env python3

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

remaining = {int(x) for x in lines[0].partition(":")[2].split()}

transformed = set()
for line in lines:
    if not line:
        remaining = remaining | transformed
        transformed = set()
        continue
    if not line[0].isdigit():
        continue
    dst, src, rng = [int(x) for x in line.split()]
    for item in list(remaining):
        if src <= item < (src + rng):
            transformed.add(dst + (item - src))
            remaining.remove(item)

remaining = remaining | transformed
print(min(remaining))
