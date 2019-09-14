import os
import csv
counter = 0
csvpath = os.path.join("budget_data.csv")
#set all variables to change
total_months = 0
profit_loss_total = 0
prev_profit_loss = 0
changes_profits_each_month = []
#avg_change = profit_loss_total / total_months 
greatest_increase_in_profit = ["Month-Year", 0]
greatest_decrease_in_profit = ["Month-Year", 999999999]

#open csv file
with open(csvpath) as financial_data:
    reader = csv.reader(financial_data)
    #skip header row
    header = next(reader)
    #loop through csv file
    for row in reader:
            #track total
            total_months = total_months +1
            
            #track total profit loss
            profit_loss_total = profit_loss_total + int(row[1])
            
            #track average profit loss change
            change_per_month = int(row[1]) - prev_profit_loss
            changes_profits_each_month.append(change_per_month)
            
            #calculate greatest increase
            if change_per_month > greatest_increase_in_profit[1]:
              greatest_increase_in_profit[0] = row[0]
              greatest_increase_in_profit[1] = change_per_month

            #calculate the greatest decrease
            if change_per_month < greatest_decrease_in_profit[1]:
              greatest_decrease_in_profit[0] = row[0]
              greatest_decrease_in_profit[1] = change_per_month
            
avg_change = profit_loss_total / total_months
average_change_per_month = sum(changes_profits_each_month)/ len(changes_profits_each_month)

#print all variables from above
print(total_months)
print(f"Average change: {avg_change}")
print(f"Average change per month: {average_change_per_month}") 

  #```text
 # Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)