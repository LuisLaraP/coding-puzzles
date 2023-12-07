#! /usr/bin/env python3

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

result = 0
for line in lines:
    line = line.partition(":")[2]
    head, tail = line.split("|")
    winning = {int(x) for x in head.split()}
    mine = {int(x) for x in tail.split()}
    hits = winning & mine
    if (n := len(hits)) > 0:
        points = 2 ** (n - 1)
    else:
        points = 0
    result += points
print(result)
