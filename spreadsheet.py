from openpyxl import Workbook
import pandas as pd
import shutil
import os

####Import Data From Location in Computer Directory####
data2 = pd.read_excel('testRunSkaters.xlsx')
#file = r'C:\Users\Matt Hellmann\Downloads\DKSalaries.csv'
#target = r'C:\Users\Matt Hellmann\PycharmProjects\learnPython\DKSalaries.csv'
#shutil.copyfile(file, target)


dataDK = pd.read_csv('DKSalaries.csv', skiprows=7, usecols=['Position', 'Name', 'Salary'])
dataDK= dataDK.rename(columns={"Name": "Player"})

####Print only some columns to view####
#print(data2[['Player', 'S','BLK']])


####Print Data filtered by a text qualifier####
#print(data2.loc[data2['Pos'] == "C"])

####Print Data sorted by a column's value####
#print(data2.sort_values('S',ascending=False))

####Create new Columns####
data2['Things'] = data2['S']+data2['BLK']
data2['Things/GP'] = ((data2['S']+data2['BLK'])/data2['GP']).round(decimals=3)
data2['Average TOI'] = ((data2['TOI'])/data2['GP']).round(decimals=3)
data2['Things/M'] = ((data2['S']+data2['BLK'])/data2['TOI']).round(decimals=3)
data2['Floor'] = (((data2['S']*1.5)+data2['BLK']*1.3)/data2['GP']).round(decimals=3)
data2 = data2.drop_duplicates(subset=['username'])

data2Slim = data2.loc[(data2['GP'] > 5) & (data2['Floor'] > 2)]


dataThings = data2Slim[['Player', 'GP', 'Average TOI', 'S', 'BLK', 'Things', 'Things/GP', 'Things/M', 'Floor']]
#print(dataThings)

dkSkate = pd.merge(dataDK, dataThings, on="Player", how="inner")
print(dkSkate)
####Upload your table to a CSV file####
#dataThings.to_csv("thingsData.csv", index=False)
