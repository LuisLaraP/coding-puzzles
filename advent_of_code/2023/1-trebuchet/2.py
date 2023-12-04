#! /usr/bin/env python3

stringmap = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

total = 0
for line in lines:
    # First digit
    first = ''
    min_idx = len(line)
    for src, dst in stringmap.items():
        idx = line.find(src)
        if idx >= 0 and idx < min_idx:
            first = dst
            min_idx = idx
    # Last digit
    last = ''
    max_idx = -1
    for src, dst in stringmap.items():
        idx = line.rfind(src)
        if idx >= 0 and idx > max_idx:
            last = dst
            max_idx = idx
    total += int(first + last)

print(total)
