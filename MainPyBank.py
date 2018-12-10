import os
import csv


budgetdatacsv= os.path.join('Resources',"budget_data.csv")
#print os.path.abspath("budget_data.csv")
   
Months = []
Profit =[]
Totalmonths = []
Total = []
AveChange = []
Avedate = []
PrevProfitLoss = []
Totalchange = 0.00
Netamount = []
x = 0
y= 0.00
with open(budgetdatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
 
    for row in csvreader:
        Months.append(row[0])
print ("Financial Analysis")    
print ("----------------------")   
print ("Total Months  " + str(len(Months)))

with open(budgetdatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        Netamount.append(int(row[1]))
        x = (sum(Netamount))
print('Total   ${:,}'.format(x))       

with open(budgetdatacsv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        Profit.append(int(row[1]))
        Avedate.append(row[0])

for i in range(len(Profit)-1):
    AveChange.append(Profit[i+1] - Profit[i])

y = (float(sum(AveChange))/len(AveChange))
minindex = AveChange.index(min(AveChange))
maxindex = AveChange.index(max(AveChange))
    #print(Avedate[minindex +1])
    #print(Avedate[maxindex +1])
print ("Average Change: $%0.2f" % (y))
    #print (min(AveChange))
print ("Greatest Increase in Profits :  " + Avedate[maxindex +1]  + " ($%0.2f)" % max(AveChange))
print ("Greatest Decrease in Profits :  " + Avedate[minindex +1]  + " ($%0.2f)" % min(AveChange))



