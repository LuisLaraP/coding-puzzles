#! /usr/bin/env python3

import re

num_re = re.compile(r"[0-9]+")

non_syms = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", }

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

result = 0
for i, line in enumerate(lines):
    for match in num_re.finditer(line):
        start_idx = match.start()
        end_idx = match.end()
        if start_idx > 0 and line[start_idx-1] not in non_syms:
            result += int(match.group())
        if end_idx < len(line) - 1 and line[end_idx] not in non_syms:
            result += int(match.group())
        look_start = max(start_idx - 1, 0)
        look_end = min(end_idx + 1, len(line))
        if i > 0 and not all(x in non_syms for x in lines[i-1][look_start:look_end]):
            result += int(match.group())
        if i < len(lines) - 1 and not all(x in non_syms for x in lines[i+1][look_start:look_end]):
            result += int(match.group())
print(result)
