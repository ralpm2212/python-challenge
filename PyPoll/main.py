import os
import csv

#resource path
pollCSV = os.path.join('/Users/dj_pc/Downloads/Starter_Code/PyPoll/Resources/election_data.csv')

#open csv and set header
with open(pollCSV) as csvfile:
    csvReader = csv.reader(csvfile)
    csvHeader = next(csvReader)

    #set variables
    totalVotes = 0
    candidateVotes = {}
    winnerCount = 0
    percentVotes = {}

    #loop through candidates
    for row in csvReader:

        #total votes cast
        totalVotes = totalVotes + 1

        #list candidates and number of votes
        if row[2] in candidateVotes:
            candidateVotes[row[2]] += 1
        else: candidateVotes[row[2]] = 1

        #percent of votes for each candidate
        for key, value in candidateVotes.items():
            percentVotes[key] = round((value/totalVotes)* 100, 3)

        #winner
            if candidateVotes[key] > winnerCount:
                winnerCount = candidateVotes[key]
                winner = key

#print results
print(f"Election Results")
print()
print(f"--------------------")
print()
print(f"Total Votes: {totalVotes}")
print()
print(f"--------------------")
print()
for key, value in candidateVotes.items():
    print(key,':' , str(percentVotes[key]),'%','(',candidateVotes[key],')')
print()
print(f"--------------------")
print()
print(f"Winner: {winner}")
print()
print(f"--------------------")

#set output file and write code in csv
output_file = "election_results.txt"
with open(output_file, "w") as text:
    text.write(f"Election Results\n")
    text.write(f"-------------------------\n")
    text.write(f"Total Votes: {totalVotes}\n")
    text.write("-------------------------\n")
    for key, value in candidateVotes.items():
        text.write(f"{key}: {str(percentVotes[key])}%   ({candidateVotes[key]})\n")
    text.write(f"-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"-------------------------\n")