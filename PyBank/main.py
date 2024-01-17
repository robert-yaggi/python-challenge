
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import os
import csv


#join csv path
budget_data = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

#Profit and Losses 
    Profit = []
    months = []

#read the csv file for data after the header
    for rows in csvreader:  
        Profit.append(int(rows[1]))
        months.append(rows[0])

    #Revenue change 
    revenue = []

    for x in range(1, len(Profit)):
        revenue.append((int(Profit[x]) - int(Profit[x-1])))


#calculation for average revenue 
revenue_average_change = sum(revenue)/ len(revenue)
average_revenue = round(revenue_average_change, 2)


#total length of months
total_months = len(months)

#greatest increase and decrease calc
greatest_increase = max(revenue)

greatest_decrease = min(revenue)


#print results table
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(Profit)))
print("Average Change" + "$" + str(average_revenue))
print("Greatest Increase in Profits: " + str(months[revenue.index(max(revenue))+1]) + " " + "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(months[revenue.index(min(revenue))+1]) + " " + "($" + str(greatest_decrease) + ")")

#generate text file 
file = open("output.txt", "w")
file.write("Financial Analysis" + "/n")
file.write("----------------------------" + "/n")
file.write("Total Months: " + str(total_months) + "/n")
file.write("Total: " + "$" + str(sum(Profit)) + "/n")
file.write("Average Change" + "$" + str(average_revenue) + "/n")
file.write("Greatest Increase in Profits: " + str(months[revenue.index(max(revenue))+1]) + " " + "($" + str(greatest_increase) + ")/n")
file.write("Greatest Decrease in Profits: " + str(months[revenue.index(min(revenue))+1]) + " " + "($" + str(greatest_decrease) + ")/n")