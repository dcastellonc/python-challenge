import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

#Creating array to store csv file data
election_results = []

#Reading CSV
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        election_results.append(row)

#Determine total votes
total_votes = len(election_results)

#Creating dictionary to count votes per candidate
candidates = {}
for x in election_results:
    if x[2] in candidates:
        candidates[x[2]] += 1
        
    else:
        candidates[x[2]] = 1

# Saving percentage of votes to dictionary
for candidate, votes in candidates.items():
    vote_percentage = round((votes/total_votes)*100,3)
    candidates[candidate] = (votes,vote_percentage)

#Separating info by candidate: percentage of votes each candidate won and total number of votes each candidate won

# Charles (1)
candidate_1 = list(candidates)[0]   
values_1 = list(candidates.values())[0]

votes_1 = (values_1[0])
percentage_1 = (values_1[1])

# Diana (2)
candidate_2 = list(candidates)[1]   
values_2 = list(candidates.values())[1] 

votes_2 = (values_2[0])
percentage_2 = (values_2[1])

# Raymon (3)
candidate_3 = list(candidates)[2]   
values_3 = list(candidates.values())[2] 

votes_3 = (values_3[0])
percentage_3 = (values_3[1])

# Determine winner
winner = max(candidates, key=candidates.get)

    
# Summary Table
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"{candidate_1}: {percentage_1}% ({votes_1})")
print(f"{candidate_2}: {percentage_2}% ({votes_2})")
print(f"{candidate_3}: {percentage_3}% ({votes_3})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# #Text File    
output_file = os.path.join("analysis","election_results.txt")   
with open(output_file, "w") as datafile:
   
    datafile.write(f"Election Results \n")
    datafile.write(f"-------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write(f"-------------------------\n")
    datafile.write(f"{candidate_1}: {percentage_1}% ({votes_1})\n")
    datafile.write(f"{candidate_2}: {percentage_2}% ({votes_2})\n")
    datafile.write(f"{candidate_3}: {percentage_3}% ({votes_3})\n")
    datafile.write(f"-------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write(f"-------------------------")