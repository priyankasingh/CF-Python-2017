#This script removes header line from CSV file.

with open("../data/CCtemperature.csv",'r') as f:
    with open("../data/Updated_CCtemperature.csv",'w') as f1:
        f.readline() # skip header line
        for line in f:
            f1.write(line) 
