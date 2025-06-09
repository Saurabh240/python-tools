# Reads and manipulates CSV files.

import csv

with open('data.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
