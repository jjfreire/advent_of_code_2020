import csv

input_file = []

with open('input.txt', newline='') as f:
    for row in csv.reader(f):
        input_file.append(int(row[0]))
        
for i in range(len(input_file)):
    for j in range(i, len(input_file)):
        amount = input_file[i] + input_file[j]
        if (amount == 2020):
            print(input_file[i] * input_file[j])

