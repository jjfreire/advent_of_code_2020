import csv

input_file = []

with open('input.txt', newline='') as f:
    for row in csv.reader(f):
        input_file.append(row[0])

valid_passwords = 0

for password in input_file:
    pos_1, pos_2 = password.split(' ')[0].split('-')
    pos_2 = int(pos_2) - 1
    pos_1 = int(pos_1) - 1
    letter = password.split(' ')[1][:-1]
    password = password.split(' ')[2]
    if ((password[pos_1] == letter) ^ (password[pos_2] == letter)):
        valid_passwords += 1

print(valid_passwords)

    