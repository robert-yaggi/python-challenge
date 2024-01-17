#PyPoll

import os
import csv

#open and read the csv file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    

    #assigning and declaring varaibles
    votes = []
    county = []
    candidates_list =[]
    CCS = []
    DD = []
    RAD = []
    CCS_votes = 0
    DD_votes = 0
    RAD_votes = 0

#read data for each row following the header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates_list.append(row[2])

# Total vote count
        total_votes = (len(votes)) 

#If/Else for Candidate votes 
    for candidate in candidates_list:
        if candidate == "Charles Casper Stockham":
            CCS.append(candidates_list)
            CCS_votes = len(CCS)
        
        elif candidate == "Diana DeGette":
            DD.append(candidates_list)
            DD_votes = len(DD)

        else:
            RAD.append(candidates_list)
            RAD_votes = len(RAD)

#Calculate vote percentages 
CCS_percentage = round(((CCS_votes/total_votes) * 100), 3)
DD_percentage = round(((DD_votes/total_votes) *100), 3)
RAD_percentage = round(((RAD_votes/total_votes) * 100), 3)

#If/Else to determine the winner
if CCS_percentage > max(DD_percentage, RAD_percentage):
    winner = "Charles Casper Stockham"
elif DD_percentage > max(CCS_percentage, RAD_percentage):
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"


#print results table
print("Election Results")
print("-------------------------") 
print("Total Votes: " + str(total_votes))
print("-------------------------") 
print("Charles Casper Stockham: " + str(CCS_percentage)+"% " + str(CCS_votes))
print("Diana DeGette: " + str(DD_percentage)+"% " + str(DD_votes))
print("Raymon Anthony Doane: " + str(RAD_percentage)+"% " + str(RAD_votes))
print("-------------------------") 
print("Winner: " + str(winner))
print("-------------------------") 

#Output to text file
file = open("output.txt","w")
file.write("Election Results")
file.write("-------------------------") 
file.write("Total Votes: " + str(total_votes))
file.write("-------------------------") 
file.write("Charles Casper Stockham: " + str(CCS_percentage)+"% " + str(CCS_votes))
file.write("Diana DeGette: " + str(DD_percentage)+"% " + str(DD_votes))
file.write("Raymon Anthony Doane: " + str(RAD_percentage)+"% " + str(RAD_votes))
file.write("-------------------------") 
file.write("Winner: " + str(winner))
file.write("-------------------------")
