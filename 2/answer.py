import csv

input_file = []

with open('input.txt', newline='') as f:
    for row in csv.reader(f):
        input_file.append(row[0])

valid_passwords = 0

for password in input_file:
    appearances_min, appearances_max = password.split(' ')[0].split('-')
    appearances_max = int(appearances_max)
    appearances_min = int(appearances_min)
    letter = password.split(' ')[1][:-1]
    password = password.split(' ')[2]
    appearances = password.count(letter)

    if (appearances >= appearances_min and appearances <= appearances_max):
        valid_passwords += 1

print(valid_passwords)

    