import os
import csv

#resource path
bankCSV = os.path.join('/Users/dj_pc/Desktop/Assignments/python-challenge/PyBank/Resources/budget_data.csv')



with open(bankCSV) as csvfile:
        csv_reader = csv.reader(csvfile)
        #stores the header row
        csv_header = next(csv_reader)

        totalMonths = 0
        netAmmount = 0
        secondRow = 0
        firstRow = 0
        monthChange = 0
        totalMonthChange = []
        date = []

        #loop through months
        for row in csv_reader:

                #Count the number of months in the dataset
                totalMonths += 1

                #Calculates the net amt of profit and losses
                firstRow = int(row[1])
                netAmmount += int(row[1])

                #Calculates average in change month to month
                if (totalMonths==1):
                        secondRow = firstRow

                else:
                        monthChange = firstRow - secondRow
                        date.append(row[0])
                        totalMonthChange.append(monthChange)
                        secondRow = firstRow
        average = round(sum(totalMonthChange)/(totalMonths - 1), 2)

        #greatest increase & decrease in profits
        greatestIncrease = max(totalMonthChange)
        greatestDecrease = min(totalMonthChange)

        increaseDate = date[totalMonthChange.index(greatestIncrease)]
        decreaseDate = date[totalMonthChange.index(greatestDecrease)]

#prints all results
print("Financial Analysis")
print()
print("-----------------------")
print()
print(f"Total Months: {totalMonths}")
print()
print(f"Total: ${netAmmount}")
print()
print(f"Average Change: ${average}")
print()
print(f"Greatest Increase in Profits: {increaseDate}(${greatestIncrease})")
print()
print(f"Greatest Decrease in Profits: {decreaseDate}(${greatestDecrease})")

#set output file and write code in csv
output_file = "fiancial_analysis.txt"        
with open(output_file, "w") as text:
        text.write(f"Financial Analysis\n")
        text.write(f"-------------------\n")
        text.write(f"Total Months: {totalMonths}\n")
        text.write(f"Total: ${netAmmount}\n")
        text.write(f"Average Change: ${average}\n")  
        text.write(f"Greatest Increase in Profits: {increaseDate}(${greatestIncrease})\n")      
        text.write(f"Greatest Decrease in Profits: {decreaseDate}(${greatestDecrease})")
        
  