import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x = [100, 200, 300]
y = [4, 2, 3]
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Test Plot')
plt.xticks([100, 200, 300], ["1h", "2h", "3h"])
plt.yticks([4, 2, 3], ["four", "two", "three"])
plt.text(1550, 71, 'India')
z = np.array(y) * 20
plt.scatter(x, y, s=z)
plt.show()
plt.clf()  # cleans it up again so you can start afresh.
# plt.scatter(x,y)
# plt.xscale('log') # TO show in the log format
plt.hist(y)
plt.hist(y, bins=5)
plt.show()
#################################################################
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')
# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris',
          'germany': 'berlin', 'norway': 'oslo', 'c': 'd'}
europe['spain'] = 'b'  # updates the dictionary
europe['italy'] = 'rome'  # updates the dictionary
del europe['c']
print('italy' in europe)
# Print out the keys in europe
print(europe.keys())
# Print out value that belongs to key 'norway'
print(europe['norway'])

# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}


# Print out the capital of France
europe['france']['capital']

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)


# Build cars DataFrame
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

cars = pd.read_csv('cars.csv')
cars = pd.read_csv('cars.csv', index_col=0)
print(cars)
# Print out country column as Pandas Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:
# cars[0:5]
# Print out fourth, fifth and sixth observation
# print(cars[3:6])

# Print out observation for Japan - This is like a time series
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt - This is like a data frame
print(cars.loc[['AUS', 'EG']])
# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr == True]

# sel = cars[cars['drives_right']]
# sel = cars[cars['drives_right'] == True]
# Print sel
print(sel)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]


# Print medium
print(medium)

# loc is for labels and iloc is for index

# cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JPN           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True


# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
