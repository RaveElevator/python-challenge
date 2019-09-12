import os
import csv
counter = 0
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    csv_header = next(csvreader)

  #  for row in csvreader:
   #     print(row)

        # count number of rows
   # with open(read_file, "r", newline = "") as pyBankFile:
       # Set CSV Reader
     #  csvreader = csv.reader(pyBankFile, delimiter = ',')
       # Count number of rows and subtract 1 for the header to get total months
       # Also, put rows into a list for later analytics fun
   #    for row in csvreader:
  #         counter = counter+1
   #        csvRows.append(row)
#   * The total number of months included in the dataset
    for row in csvreader:
           counter = counter+1
print(counter)
        
#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period