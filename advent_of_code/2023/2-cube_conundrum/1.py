#! /usr/bin/env python3

with open("input.txt", "r") as input_file:
    games = input_file.readlines()

result = 0
for game in games:
    red = green = blue = 0
    head, tail = game.split(":")
    game_id = int(head.split()[1])
    for turn in tail.split(";"):
        splitline = [s.split() for s in turn.split(",")]
        sets = {x[1].strip(): int(x[0].strip()) for x in splitline}
        red = max(red, sets.get("red", 0))
        green = max(green, sets.get("green", 0))
        blue = max(blue, sets.get("blue", 0))
    if red <= 12 and green <= 13 and blue <= 14:
        result += game_id
print(result)
