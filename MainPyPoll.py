import os
import csv

NameList=[]
Total = []
Avevote = []
Voteperperson = 0
Totalvote = []
mydict = dict()
winner = dict()
x = 0
y= 0.00


Polldatacsv= os.path.join ("Resources","election_data.csv")


with open(Polldatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
       Totalvote.append(row[0])


with open(Polldatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        NameList.append(row[2])


myset = set(NameList)
Uniquenames = list(myset)


with open(Polldatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        name = row[2]
        voterID = row[0]
        mydict.setdefault(name,[]).append(voterID)

x = len(Totalvote)

print ("Election Results") 
print                   
print ("----------------------")  
print                   
print ("Total Votes: " + str(x))
print                 
print ("----------------------")
print                  

for k in mydict:
    y = len(mydict[k])
    print (str(k)  + ":       %0.3f" %(y * 100.00/x) + "%  (" + str(y)+")")
    winner.update({k:y})

max_votes = max(winner.values()) 
winner_name = [k for k, v in winner.items() if v == max_votes]
print ("----------------------")
print ("Winner:    " + winner_name[0])
print ("----------------------")







