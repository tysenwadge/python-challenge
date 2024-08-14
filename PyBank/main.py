#Importing the necessary libraries
import os
import csv

#storing csv file in object
budget_data = os.path.join("Resources","budget_data.csv")

#set variables
month_total = 0
profit_loss = 0
csv_value = 0
amt_change = 0
dates = []
profit_amt = []

#Opening/reading the budget_data CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Starting with the header row
    csv_header = next(csvreader)

    #Now Reading the first row and track changes
    first_row = next(csvreader)
    month_total += 1
    profit_loss += int(first_row[1])
    csv_value = int(first_row[1])
    
    #Go through each row 
    for row in csvreader:
        # Append and keep track of the dates
        dates.append(row[0])
        
        # Calculate the change and store it
        amt_change = int(row[1])-csv_value
        profit_amt.append(amt_change)
        csv_value = int(row[1])
        
        #Add to total number of months
        month_total += 1

        #Total Profit/Losses for time period
        profit_loss = profit_loss + int(row[1])

    #Calculate the Greatest decrease in profits 
    gt_decrease = min(profit_amt)
    wst_index = profit_amt.index(gt_decrease)
    wst_date = dates[wst_index]
    
    #Calculate the Greatest increase in profits
    gt_increase = max(profit_amt)
    grt_index = profit_amt.index(gt_increase)
    gt_date = dates[grt_index]


    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profit_amt)/len(profit_amt)
    

#Displaying the output and formatting
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(month_total)}")
print(f"Total: ${str(profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {gt_date} (${str(gt_increase)})")
print(f"Greatest Decrease in Profits: {wst_date} (${str(gt_decrease)})")

#Exporting to the .txt file in Analysis folder
output = open("Analysis/output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(month_total)}")
line4 = str(f"Total: ${str(profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {gt_date} (${str(gt_increase)})")
line7 = str(f"Greatest Decrease in Profits: {wst_date} (${str(gt_decrease)})")
#Online example for formatting output
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))