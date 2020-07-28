# bring in dependencies
import os
import csv

# store file to variable
bank = os.path.join ("Resources","pybank_budget_data.csv")

# listing variables that I will fill later on
m_list = []
p_list = []
total_PL = 0
avg_chg = []
max_date = 0
min_date = ""

# opening the csv file to read
with open(bank, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    
    #Tried List Comprehensions here - failed miserably
    # total_PL = [(row[1]) for row in csvreader]
    
    # generating a list containing all of the dates
    # m_list = [(row[0]) for row in csvreader]
    
    # Filling my months and profits list, as well as generating the total profit/losses number
    for row in csvreader:
        m_list.append(row[0])
        p_list.append(int(row[1]))
        total_PL += int(row[1])
    
    # generating variable to contain total number of months and total Profit/Loss in the dataset
    months = len(m_list)  
    
    # Getting the average amount changed
    for x in range(len(p_list)-1):
        avg_chg.append(p_list[x+1]-p_list[x])
        
    change = round((sum(avg_chg) / len(avg_chg)),2)

    # calculating the great increase and decreases in profits
    max_p = max(avg_chg)
    min_p = min(avg_chg)
    
    # finding the months with the greatest increase and decreases in profits
    # I had to google to find this solution out
    #
    # Essentially, you are trying to find the 'Index Location' for the number with the highest profits, then you will
    # reference that same index to get the month in your print statement
    
    max_month = avg_chg.index(max_p) + 1
    min_month = avg_chg.index(min_p) + 1
    
#Print Statements

print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {months}')
print(f'Total:{total_PL}')
print(f'Average Change: ${change}')
print(f'Greatest Increase in Profits: {m_list[max_month]} (${max_p})')
print(f'Greatest Decrease in Profits: {m_list[min_month]} (${min_p})')

#Output

output_file = os.path.join ("Analysis","CHG_pybankOutput.txt")
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis \n")
    textfile.write("------------------------- \n")
    textfile.write(f'Total Months: {months}\n')
    textfile.write(f'Total:{total_PL}\n')
    textfile.write(f'Average Change: ${change}\n')
    textfile.write(f'Greatest Increase in Profits: {m_list[max_month]} (${max_p})\n')
    textfile.write(f'Greatest Decrease in Profits: {m_list[min_month]} (${min_p})')
    




