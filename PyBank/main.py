import os
import csv

# Path to collect data from the Resources folder
findataCSV = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(findataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # count the number of months included in the dataset
    data = list(csvreader)
    row_count = len(data)
    diff_pl = 0
    sum_pl = 0
    sum_diff_pl = 0
   
    # num_months = 0
    prev_row_pl = data[1]
    for i in range(2, row_count): 
        diff_pl = float((data[i][1]) - (prev_row_pl[1]))
        sum_pl += float(data[i][1])
        sum_diff_pl += diff
        average = sum_diff_pl / row_count
        prev_row_pl = data[i] 

print("Financial Analysis:")
print("Total Months: " + str(row_count))  
print("Total: " + str(sum_pl))
print("Average Change: " + str(average))   

        

