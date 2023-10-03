#Import functions
import os
import csv

#Make some variables for later
total = 0
can=[] #Candidate List
VoteP = [] #Percentage of votes
VoteT = [] #Total votes each candidate
Win = "" #Winner of election



#directory
csvpath=os.path.join('..', 'pypoll','resources','election_data.csv')
print("Election Results")
print("------------------------------------------------------------")

#Opens the csv 
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')    
    header = next(csvreader)
    for row in csvreader:
        total += 1 #tallies all votes
        
        #Filter candidates to list, and tally their votes
        if row[2] not in can: #google bard helped get this line to run
            can.append(row[2])
            index = can.index(row[2])
            VoteT.append(1)
        else:
            index = can.index(row[2])
            VoteT[index] += 1
        
#Detemine Percentage of votes
for votes in VoteT:
    pcnt = (votes/sum(VoteT)) * 100
    pcnt = round(pcnt)
    pcnt = "%.3f%%" % pcnt
    VoteP.append(pcnt)

#Determine winner
    Win = max(VoteT)
    index = VoteT.index(Win)
    Win= can[index]

#print the final analysis
print(f"Total Votes: " , total)
print("------------------------------------------------------------")
for i in range(len(can)):
    print(f"{can[i]}: {str(VoteP[i])} ({str(VoteT[i])})")
print("------------------------------------------------------------")
print(f"Winner: ", Win)
print("------------------------------------------------------------")

#export to .txt
output2=os.path.join('..', 'pypoll','output2.txt')
with open(output2, 'w') as output:
    output.write("Election Results\n")
    output.write("------------------------------------------------------------\n")
    output.write(f"Total Votes: {total}\n")
    output.write("------------------------------------------------------------\n") 
    for i in range(len(can)):
        output.write(f"{can[i]}: {str(VoteP[i])} ({str(VoteT[i])})\n")
    output.write("------------------------------------------------------------\n")    
    output.write(f"Winner: {Win}\n")
    output.write("------------------------------------------------------------\n")    
