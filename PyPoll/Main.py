import os
import csv
csvpath = os.path.join("election_data.csv")

counter = 0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:

        counter += 1
print(counter)

print(f'Number of votes: {counter}')