
# import dependencies
import os, csv

# import file from folder
polls = os.path.join ("Resources","pypoll_election_data.csv")

# creating my variables
votes_cast = []
candidates = []
k_count = 0
c_count = 0
l_count = 0
o_count = 0

# opening the file to read in the information
with open(polls,encoding='utf-8') as file:
    pollData = csv.reader(file,delimiter=',')
    csv_header = next(pollData)
    
    # This block of data will give me a list of Voter ID numbers
    # as well as populated my candidates list with all of the candidates
    # and this will also 
    for row in pollData:
        
        votes_cast.append(row[0])
        
        candidates.append(row[2])
        
        if row[2] == "Khan":
            k_count += 1
        elif row[2] == "Correy":
            c_count += 1
        elif row[2] == "Li":
            l_count += 1
        elif row[2] == "O'Tooley":
            o_count += 1

# This block of code will give me the list of candidates people 
       # voted for in this election period
       #unique_can = []
   #for candidate in candidates:
       #if candidate not in unique_can:
           #unique_can.append(candidate)

# generate total votes
total_votes = len(votes_cast)

#generate candidate percentages
k_percent = (k_count / total_votes) * 100
c_percent = (c_count / total_votes) * 100
l_percent = (l_count / total_votes) * 100
o_percent = (o_count / total_votes) * 100

# selecting the winner of the election
# found online that making a dictionary out of the items would be best
results = {"Khan":k_count,
          "Correy":c_count,
          "Li":l_count,
          "O'Tooley":o_count}

# I found this code online - essentially what I'm doing here is calling a max function
# on my results list, then calling a get function on the key
winner = max(results, key=results.get)

# Print Statements
print("Election Results")
print("------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------")
print(f'Khan: {k_percent:.3f}% ({k_count})')
print(f'Correy: {c_percent:.3f}% ({c_count})')
print(f'Li: {l_percent:.3f}% ({l_count})')
print(f"O'Tooley: {o_percent:.3f}% ({o_count})")
print("------------------------")
print(f'Winner: {winner}')
print("------------------------")

# Output

output_file = os.path.join ("Analysis","CHG_pypollOutput.txt")
with open(output_file, "w") as textfile:
    textfile.write("Election Results \n")
    textfile.write("------------------------ \n")
    textfile.write(f'Total Votes: {total_votes}\n')
    textfile.write("------------------------ \n")
    textfile.write(f'Khan: {k_percent:.3f}% ({k_count})\n')
    textfile.write(f'Correy: {c_percent:.3f}% ({c_count})\n')
    textfile.write(f'Li: {l_percent:.3f}% ({l_count})\n')
    textfile.write(f"O'Tooley: {o_percent:.3f}% ({o_count})\n")
    textfile.write("------------------------ \n")
    textfile.write(f'Winner: {winner}\n')
    textfile.write("------------------------")