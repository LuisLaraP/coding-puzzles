#! /usr/bin/env python3

with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

total = 0
for line in lines:
    first = ''
    last = ''
    i = 0
    while not line[i].isdigit():
        i += 1
    first = line[i]
    i = len(line) - 1
    while not line[i].isdigit():
        i -= 1
    last = line[i]
    total += int(first + last)

print(total)
