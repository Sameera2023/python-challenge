# Module for OS
import os

# Module for reading CSV files
import csv

# Assigning the resource file path
csvpath = os.path.join(r'\Users\samee\python-challenge\PyBank', 'Resources', 'budget_data.csv')


Months = []         #List for months
ProfitorLoss = []   # List for Profilt/Loss amount
Change = []         # List to calculate average change

# Reading the Budget Data CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Writing the first colum & second column to lists
    for row in csvreader:
        Months.append(row[0])
    
        ProfitorLoss.append(row[1])

    # Printing the Total months
    print("Total Months: " + str(len(Months)))
    
    # Calculating the total Profit/Loss
    # Setting the initial value to zero
    Total = 0
    for i in range(0, len(ProfitorLoss)):
        Total = Total + int(ProfitorLoss[i])
    # Printing the Total of Profit/Loss
    print("Total: $",Total)
    

    # Calculation of Average change in Profit/Loss 
    # Writing the change from each row/month to list
    for i in range(0, len(ProfitorLoss)-1):
        change = int(ProfitorLoss[i+1]) -  int(ProfitorLoss[i])
        Change.append(int(change))
    
    # Function to calculate average change
    def average(ChangeList):
        length = len(ChangeList)
        total = 0.0
        for number in ChangeList:
            total += number
        return total / length
    
    # Calling Average function
    AverageChange = round(average(Change), 2)

    # Printing average change in Profit/Loss
    print("Average Change: $", AverageChange)
    
    
    # Finding greatest increase in profit/loss
    GreatestIncrease = 0
    # For loop to find the greatest increase
    for i in range(0, len(ProfitorLoss)-1):
      diff =  int(ProfitorLoss[i+1]) -  int(ProfitorLoss[i])
      if diff > GreatestIncrease :
          GreatestIncrease = diff
          GIMonth = i+1
        
    # Printing the Greatest increase
    print(f"Greatest Increase in Profits: {Months[GIMonth]} (${GreatestIncrease}) ")
    

    
    # Finding Greatest Decrease in Profits
    Greatestdrop = 0  

    # For loop to find the greatest decrease in profit/loss
    for i in range(0, len(ProfitorLoss)-1):
        if int(ProfitorLoss[i+1]) < int(ProfitorLoss[i]):
            drop = int(ProfitorLoss[i+1]) -  int(ProfitorLoss[i])
            if drop < Greatestdrop :
                Greatestdrop =  drop
                GDMonth = i+1
              

    # Printing the greatest decrease    
    print(f"Greatest Decrease in Profits: {Months[GDMonth]} (${Greatestdrop}) ")
    
    
  

# Writing the output file to text file

with open('output.txt', 'w') as f:
        f.writelines(f"""Financial Analysis
----------------------------
Total Months:  { str(len(Months))}
Total:  ${Total}
Average Change: ${AverageChange}
Greatest Increase in Profits: {Months[GIMonth]} (${GreatestIncrease})
Greatest Decrease in Profits: {Months[GDMonth]} (${Greatestdrop})""")       

        f.close()
        

    

    