#This script will remove headers from a CSV file

with open("../data/CCtemperature.csv",'r') as f:
    with open("../data/CCtemp_nohead.csv",'w') as f1:
        f.readline() #reading every row from f
        for line in f:
            f1.write(line) 
