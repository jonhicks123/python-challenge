# import csv file
import os
import csv

# set the path for the budget data csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# read in csv file
with open(budget_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # set variables
    Months = []
    ProfLoss = []
    MonthChange = []
    AvgChange = []
    GI = []
    GD = []
    GIdate = ""
    GDdate = ""

    # find total months and total profits/losses
    for row in csvreader:
        Months.append(row[0])
        ProfLoss.append(int(row[1]))
    
    for x in range(1, len(ProfLoss)):
        # get Monthly average change
        MonthChange.append(int(ProfLoss[x]) - int(ProfLoss[x-1]))
        AvgChange = sum(MonthChange) / len(MonthChange)

        # find greatest inc and dec and their dates
        GI = max(MonthChange)
        GIdate = str(Months[MonthChange.index(max(MonthChange))+1])
        GD = min(MonthChange)
        GDdate = str(Months[MonthChange.index(min(MonthChange))+1])

    # print the output
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", len(Months))
    print("Total: $", sum(ProfLoss))
    print("Average Change: $", round(AvgChange,2))
    print("Greatest Increase in Profits: ", GIdate, "($", GI, ")")
    print("Greatest Decrease in Profits: ", GDdate, "($", GD, ")")

with open("analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {len(Months)}\n")
    txtfile.write(f"Total: $ {sum(ProfLoss)}\n")
    txtfile.write(f"Average Change: $ {round(AvgChange,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {GIdate} (${(GI)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {GDdate} (${(GD)})\n")
