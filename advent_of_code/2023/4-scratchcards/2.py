#! /usr/bin/env python3

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

copies = {i + 1: 1 for i in range(len(lines))}
result = 0
for i, line in enumerate(lines):
    card_id = i + 1
    line = line.partition(":")[2]
    head, tail = line.split("|")
    winning = {int(x) for x in head.split()}
    mine = {int(x) for x in tail.split()}
    hits = winning & mine
    for j in range(len(hits)):
        copies[card_id + j + 1] += copies[card_id]
result = sum(copies.values())
print(result)
