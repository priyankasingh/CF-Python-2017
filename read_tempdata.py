temp_data=open("../data/CCtemperature.CSV",'r')

for line in temp_data:
    print(line.rstrip())
