temp_data = open('Data/CCtemperature.csv', 'r')

def celsius_to_fahr(celsius): 
	fahr = (celsius * 9/5) + 32
	return fahr

for line in temp_data:
	data = line.split(',')
	if data[0].isalpha():
		pass
	else:

		fahr2 = celsius_to_fahr(float(data[1]))
		print('Average temperate in fahr: ', fahr2)
