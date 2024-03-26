
#import modules to read csv file
import os
import csv

#define path for the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#declare the variables and lists needed to calculate and store values
month_Count = 0
date = []
amount = 0
profit = []
avg_Change = []
max_Increase = 0
max_Decrease = 0

#open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row, since it shouldn't be included in the calculations
    next(csvreader)

    #begin reading through each row
    for row in csvreader:

        #count the # of months by iterating through each row and increasing the count by 1
        month_Count += 1
        date.append(row[0])
        

        #add all the values in column 2
        amount += int(row[1])
        profit.append(int(row[1]))

#perform calculations
for i in range (len(profit)-1):

    #average change in profit/loss per month
    month_Diff = profit[i+1] - profit[i]
    avg_Change.append(month_Diff) 

    avg_Monthly_Change = round(sum(avg_Change)/len(avg_Change),2)

    #calculate greatest increases and decreases
    if(month_Diff>max_Increase):
        max_Increase_Date = date[i+1]
        max_Increase = month_Diff
    
    if(month_Diff<max_Decrease):
        max_Decrease_Date = date[i+1]
        max_Decrease = month_Diff


#print and output to text file    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_Count}")
print(f"Total: {amount}")
print(f"Average Change: {avg_Monthly_Change}")
print(f"Greatest Increase in Profits: {max_Increase_Date} {max_Increase}")
print(f"Greatest Decrease in Profits: {max_Decrease_Date} {max_Decrease}")

txtfile_Path = os.path.join('Analysis', 'results.txt')
with open(txtfile_Path, "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {month_Count}\n")
    txtfile.write(f"Total: ${amount}\n")
    txtfile.write(f"Average Change: ${avg_Monthly_Change}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_Increase_Date} {max_Increase}\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_Decrease_Date} {max_Decrease}\n")
 