import csv
import os

# load the files

loadFile = os.path.join(r"C:\Users\junark\Desktop\python-challenge\election_data.csv")
outputFile = os.path.join("electionresults.txt")

#Counter setup
totalVotes = 0

#choice of candidate and voting counts

candidateChoice = []
candidateVotes = {}

#convert CSV to dictionary list

with open(loadFile) as election_data:
	reader = csv.DictReader(election_data)

#loop

for row in reader: 
	totalVotes = totalVotes + 1

#extract name of candidate from row

candidateName = row["Candidate"]

if candidateName not in candidateChoice:

    candidateChoice.append(candidateName)

    candidateVotes[candidateName] = 0

    candidateVotes[candidateName] = candidateVotes[candidateName] + 1

print(candidateName)

# #print results and export to notepad
# with open(outputFile, "w") as txt_file:

#     votingResults = (
#     f"Total votes are {totalVotes}"
#     )
#     print(votingResults, end="")

# # #save text file
# txt_file.write(votingResults)