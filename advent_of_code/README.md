# Advent of Code

Advent of Code is an annual event held every December where programming puzzles are published every day from Dec 1 to Dec 25, in the form of an advent calendar.

Each day, a puzzle is released, which consists of an input text file and a set of instructions. The goal is to obtain a number or a string to enter into the AoC website. The site will check if the answer is correct.

After solving the first puzzle of the day, a second puzzle, normally a harder version of the first one, will be revealed. The second puzzle uses the same input file as the first, but the instructions are different. As with the first puzzle, the objective is to calculate a string or number from the input and enter it into the website.

## Structure of solutions

Inside this directory there is one directory for each AoC year. Within a year's directory, there is one folder for each day of the event.

The directory of each day contains the following files:

	- `input.txt`. The input file, which is the same for both puzzes of the day.
	- `test_1.txt`. Test input for the first puzzle.
	- `test_2.txt`. Test input for the second puzzle.
	- Source code of the solution for the first puzzle. It is called `1.<extension>`, where the extension depends on the programming language.
	- Source code of the solution for the second puzzle. It is called `2.<extension>`, where the extension depends on the programming language.
