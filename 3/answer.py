import csv
from functools import reduce

input_file = []
slopes = []
tree = '#'

with open('input.txt', newline='') as f:
    for row in csv.reader(f):
        input_file.append(row[0])

with open('slopes.csv', newline='') as f:
    for row in csv.reader(f):
        slopes.append(row)

trees = []
mod = len(input_file[0])

for slope in slopes:
    steps_right, steps_down = slope
    steps_down = int(steps_down)
    steps_right = int(steps_right)

    slope_trees = 0
    down = 0
    right = 0
    while (down < len(input_file)):
        if (input_file[down][right] == tree):
            slope_trees += 1

        right = (right + steps_right) % mod 
        down += steps_down

    trees.append(slope_trees)



print(reduce(lambda x, y: x*y, trees))