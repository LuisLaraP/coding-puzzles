#! /usr/bin/env python3

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

splitline = [int(x) for x in lines[0].partition(":")[2].split()]
remaining = set()
for i in range(0, len(splitline), 2):
    remaining.add((splitline[i], splitline[i+1]))

transformed = set()
for line in lines:
    if not line:
        remaining = remaining | transformed
        transformed = set()
        continue
    if not line[0].isdigit():
        continue
    dst, src, rng = [int(x) for x in line.split()]
    for start, size in list(remaining):
        inter_start = max(start, src)
        inter_end = min(start + size, src + rng)
        intersection = (inter_start, inter_end - inter_start)
        if intersection[1] > 0:
            lower_rest = (start, inter_start - start)
            upper_rest = (inter_end, start + size - inter_end)
            mapped = (inter_start - src + dst, intersection[1])
            remaining.remove((start, size))
            transformed.add(mapped)
            if lower_rest[1] > 0:
                remaining.add(lower_rest)
            if upper_rest[1] > 0:
                remaining.add(upper_rest)

remaining = remaining | transformed
print(min(rng[0] for rng in remaining))
