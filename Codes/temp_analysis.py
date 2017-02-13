temp_data=open("../data/CCtemperature.csv",'r')

for line in temp_data:
    data=line.split(',')

    #Print 2nd column for average surface temperature
    print('Average surface temp: ',data[1])
