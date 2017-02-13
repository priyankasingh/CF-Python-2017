#This script converts surface temperature column from degree celsius to degree fahrenheit.
from cel_to_fahr import cel_to_fahr

temp_data=open("../data/CCtemp_nohead.csv",'r')

for line in temp_data:
    data=line.split(',')

    celsius=float(data[1])

    fahr=cel_to_fahr(celsius)
    print("Average surface temperatures in fahrenheit: ",fahr)
