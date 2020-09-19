# Importing os and csv file - Coaches, ...so hard not to type CVS :)
import os
import csv

# Create path to CSV file
budget_data = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # print header row
    print(f"Header: {csv_header}")

# Create paths
    profitLoss = []
    months = []

# Read each row of data after header
    for rows in csvreader:
        months.append(rows[0])
        profitLoss.append(rows[1])

# Calculate difference in revenue
    revenue_diff = []

for x in range(1, len(profitLoss)):
    revenue_diff.append((float(profitLoss[x]) - float(profitLoss[x-1])))
  
# Calculate average revenue difference
revenue_average = float(sum(revenue_diff) / len(revenue_diff))

# Calculate total month duration
total_months = len(months)

total = sum(map(int,profitLoss))

# Greatest increase in revenue
greatest_increase = max(revenue_diff)
# Greatest decrease in revenue
greatest_decrease = min(revenue_diff)

# Print results 
print("Financial Analysis")

print("..................")

print(f"Total Months: {total_months}")

print(f"Total: $ {total}")

print(f"Average Change: $ {round(revenue_average,2)}")

print(f"Greatest Increase in Profits: {months[revenue_diff.index(max(revenue_diff))+1]} $ {int((greatest_increase))}")

print(f"Greatest Decrease in Profits: {months[revenue_diff.index(min(revenue_diff))+1]} $ {int((greatest_decrease))}")

# Write output

with open("Analysis/output.txt", "w") as txtfile:
   
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write(".................." + "\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total: $" + str(total) + "\n")
    txtfile.write("Average Change: $" + str(round(revenue_average,2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(months[revenue_diff.index(max(revenue_diff))+1]) + " " + "$" + str(round(greatest_increase,0)) + "\n")
    txtfile.write("Greatest Decrease in Profits: " + str(months[revenue_diff.index(min(revenue_diff))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    txtfile.close()


	

	

	

	

