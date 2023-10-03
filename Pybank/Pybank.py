#Import functions
import os
import csv

#Make some variables for later
mths = 0
total = 0
chg = 0 #total change
chgl=[] #Change List
chgP = 0 #previous month value
chgavg = 0 #average change
chgm = [] #month of change
inc = ["", 0] #largest increase
dec = ["", 0] #largest decrease

#directory
csvpath=os.path.join('..', 'pybank','resources','budget_data.csv')
print("Financial analysis")
print("------------------------------------------------------------")

#Opens the csv 
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = sum(int(row[1]) for row in csvreader) #this code closes the csv so it gets its own "With"

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')    
    header = next(csvreader)
    for row in csvreader:
        mths += 1 #tallies months
        chg = int(row[1]) - chgP #31-34 finds average change (still not correct answer for some reason)
        chgP = int(row[1])
        chgl = chgl + [chg]
        chgm = [chgm] + [row[0]]
        #check increase against itself
        if chg>inc[1]:
            inc[1] = chg
            inc[0] = row[0]

        #check decrease against itself
        if chg<dec[1]:
            dec[1] = chg
            dec[0] = row[0]

#calculate change            
    chgl=chgl[1:] #list slicing! the bracket cuts the code to fit index one to the end// Assisted by AskBCS
    chgavg = sum(chgl)/len(chgl)


#print the final analysis
print(f"Total Months: ",  mths)
print(f"Total: " , total)
print(f"Average change: " , chgavg)
print(f"Greatest Increase in Profits:" , inc)
print(f"Greatest Decrease in Profits: " , dec)