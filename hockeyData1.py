import tset as tset
from openpyxl import Workbook
import pandas as pd
import shutil
import os
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd
from sklearn.linear_model import LinearRegression
import random
from scipy.stats import ttest_1samp

#print(random.randint(0,913))



####Import Data From Location in Computer Directory####
data2 = pd.read_excel('hockeydata.xlsx')
data4 = pd.read_excel('hockeydata2.xlsx')

#file = r'C:\Users\Matt Hellmann\Downloads\DKSalaries.csv'
#target = r'C:\Users\Matt Hellmann\PycharmProjects\learnPython\DKSalaries.csv'
#shutil.copyfile(file, target)



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
data4['Average TOI'] = ((data2['TOI'])/data2['GP']).round(decimals=3)
#data2['Things/M'] = ((data2['S']+data2['BLK'])/data2['TOI']).round(decimals=3)
#data2['Floor'] = (((data2['S']*1.5)+data2['BLK']*1.3)/data2['GP']).round(decimals=3)

#combines players with multiple rows due to trades
data2 = data2.drop_duplicates(subset=['Username'])
data3 = data2[['Player', 'Age', 'Average TOI']]
data5 = data4[['Player', 'Age', 'Average TOI']]

#Compute True mean
data3mean = data3["Age"].mean()

#Computer Sample Mean
data5mean = data5["Age"].mean()
print("Sample Mean: ", data5mean)

#One Sided T-Test to see if these are different:
tset, pVal = ttest_1samp(data3["Age"],data5mean)
print("P-Value: ", pVal)

#xVals = data3.iloc[:, 1].values.reshape(-1, 1)  # values converts it into a numpy array
#yVals = data3.iloc[:, 2].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

#linear_regressor = LinearRegression()  # create object for the class
#linear_regressor.fit(xVals, yVals)  # perform linear regression
#atoi_pred = linear_regressor.predict(xVals)  # make predictions

#plt.scatter(xVals,yVals)
#plt.plot(xVals,atoi_pred,color='red')
#plt.xlabel("Player Age")
#plt.ylabel("Average Time on Ice")
#plt.title("Age/Usage in the NHL")
#plt.show()


#data2Slim = data2.loc[(data2['GP'] > 5) & (data2['Floor'] > 2)]


#dataThings = data2Slim[['Player', 'GP', 'Average TOI', 'S', 'BLK', 'Things', 'Things/GP', 'Things/M', 'Floor']]
#print(dataThings)

