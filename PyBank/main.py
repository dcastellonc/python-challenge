import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')


budget_data = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        row = [row[0], int(row[1])]
        budget_data.append(row)

months= len(budget_data)
net_total = sum([x[1] for x in budget_data])

total_monthly_change = []
for i in range(len(budget_data) - 1):
    total_monthly_change.append((budget_data[i+1][1] - budget_data[i][1], budget_data[i+1][0]))

total_monthly_average = round(sum([x[0] for x in total_monthly_change])/len([x[0] for x in total_monthly_change]),2)




Increase = max(total_monthly_change)
Decrease = min(total_monthly_change)


print ("Financial Analysis")
print("---------------------------")
print (f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${total_monthly_average}")
print(f"Greatest Increase in Profits: {Increase [1]} (${Increase[0]})")
print(f"Greatest Decrease in Profits: {Decrease[1]} (${Decrease[0]})")    
    
output_file = os.path.join("analysis","analysis.txt")   
with open(output_file, "w") as datafile:
   
    datafile.write("Financial Analysis \n")
    datafile.write("--------------------------- \n")
    datafile.write(f"Total Months: {months}\n")
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f"Average Change: ${total_monthly_average}\n")
    datafile.write(f"Greatest Increase in Profits: {Increase [1]} (${Increase[0]})\n")
    datafile.write(f"Greatest Decrease in Profits: {Decrease[1]} (${Decrease[0]})\n")