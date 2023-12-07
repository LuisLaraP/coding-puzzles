#! /usr/bin/env python3

def find_number(line, init):
    start = init
    while start > 0 and line[start - 1].isdigit():
        start -= 1
    end = init
    while end < len(line) - 1 and line[end + 1].isdigit():
        end += 1
    return start, end

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

result = 0
for y, line in enumerate(lines):
    x = -1
    while (x := line.find("*", x + 1)) != -1:
        numbers = []
        start_x = max(x - 1, 0)
        end_x = min(x + 1, len(line) - 1)
        # Above
        if y > 0:
            i = start_x
            while i <= end_x:
                if lines[y - 1][i].isdigit():
                    start, end = find_number(lines[y - 1], i)
                    numbers.append(int(lines[y - 1][start:end+1]))
                    i = end + 1
                else:
                    i += 1
        # Below
        if y < len(lines) - 1:
            i = start_x
            while i <= end_x:
                if lines[y + 1][i].isdigit():
                    start, end = find_number(lines[y + 1], i)
                    numbers.append(int(lines[y + 1][start:end+1]))
                    i = end + 1
                else:
                    i += 1
        # Left
        if x > 0 and line[x - 1].isdigit():
            start, end = find_number(line, x - 1)
            numbers.append(int(line[start:end+1]))
        # Right
        if x < len(line) - 1 and line[x + 1].isdigit():
            start, end = find_number(line, x + 1)
            numbers.append(int(line[start:end+1]))
        if len(numbers) == 2:
            result += numbers[0] * numbers[1]

print(result)
