import pandas as pd

import urllib

#link="http://spreadsheets.google.com/pub?key=0ArtujvvFrPjVdERlTHZFQ2ZaUkpySHpQMF82UmdlcUE&output=xls"

#urllib.request.urlretrieve(link,"income_per_capita.xlsx")

complete_gdp=pd.read_excel('income_per_capita.xlsx')

#print(complete_gdp.head())   

#Transformation of GDP data

complete_gdp.index=complete_gdp[complete_gdp.columns[0]]
transform=complete_gdp.drop(complete_gdp.columns[0],axis=1)
transform.columns=map(lambda x:int(x),transform.columns)
transform=transform.T
print(transform.head())
