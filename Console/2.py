import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print('Hello World')

# plot,scatter,histogram#################################################################
x = [100, 200, 300]
y = [4, 2, 3]
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Test Plot')
plt.xticks([100, 200, 300], ["1h", "2h", "3h"])
plt.yticks([4, 2, 3], ["four", "two", "three"])
plt.text(5, 5, 'India', fontsize=12, color='red', alpha=0.5,
         verticalalignment='center', horizontalalignment='center')
plt.show()
plt.clf()

z = np.array(y) * 20
# Shows only the dots will not be connected, Here the third argument is for the size of the marker.
plt.scatter(x, y, s=z)
plt.show()
plt.clf()  # cleans it up again so you can start afresh.

plt.scatter(x, y)
plt.show()
plt.clf()

plt.xscale('log')  # TO show in the log format
# plt.hist(y)
# no of times the data should be divided. The default value is 10
plt.hist(y, bins=5)
plt.show()
plt.clf()

# Dictionary #################################################################

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')
print(ind_ger)  # 2

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])  # berlin

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris',
          'germany': 'berlin', 'norway': 'oslo', 'c': 'd'}

europe['spain'] = 'b'  # updates the dictionary
europe['italy'] = 'rome'  # updates the dictionary
del europe['c']  # deletes the key 'c'

# True  >> returns True if the element is present in the dictionary
print('italy' in europe)

# Print out the keys in europe
# dict_keys(['spain', 'france', 'germany', 'norway', 'italy'])
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])  # oslo


# Dictionary of dictionaries #################################################################
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}

# Print out the capital of France
print(europe['france']['capital'])  # paris

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data  # adds italy to this list

# Print europe
print(europe)
# {'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'italy': {'capital': 'rome', 'population': 59.83}}

# Build cars DataFrame from dictionary #################################################################

# creating a data frame from a dictionary
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars - Here we are trying to have row labels for each row instead of index
cars.index = row_labels

# Print cars again
print(cars)

# Build cars series/DataFrame from csv file #################################################################

cars = pd.read_csv('datasets/cars.csv')
print(cars)
# set it to 0, so that the first column is used as row labels.
cars = pd.read_csv('datasets/cars.csv', index_col=0)
print(cars)


# ************Here we are trying to select the columns ************
# Print out country column as Pandas Series
print(type(cars['country']))  # <class 'pandas.core.series.Series'>
print(cars['country'])
# print(cars['country', 'drives_right'])  #Error


# Print out country column as Pandas DataFrame
print(type(cars[['country']]))  # <class 'pandas.core.frame.DataFrame'>
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# ************Here we are trying to select the rows************
# Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame.
# The following call selects the first five rows from the cars DataFrame:

print(cars[0:5])  # This type is data frame
# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Data series implementation ##############################################################
# Print out observation for Japan - This is like a time series
# print(cars.loc['JPN'])
# cars_per_cap      588
# country         Japan
# drives_right    False
# Name: JPN, dtype: object

# print(cars.loc['AUS', 'EG']) # Error

# Print out drives_right value of Japan - Here we are trying to get the data of row and the column
print(cars.loc['JPN', 'drives_right'])  # False

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])


# Data frame implementation ##############################################################
# Print out observations for Australia and Egypt - This is like a data frame
print(cars.loc[['AUS', 'EG']])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])


# Data filtering ##############################################################

# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars[dr == True]
print(sel)
print(type(sel))  # <class 'pandas.core.frame.DataFrame'>

sel = cars[cars['drives_right']]
print(sel)
sel = cars[cars['drives_right'] == False]
print(sel)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print(medium)

# loc is for labels and iloc is for index

# Data ##
#         cars_per_cap      country       drives_right
# US            809   United States         True
# AUS           731      Australia         False
# JPN           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True
