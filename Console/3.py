import pandas as pd
import numpy as np


# Comparision #################################################################
print(2 == (1 + 1))  # True
print("intermediate" != "python")  # True
print(True != False)  # True
print("Python" != "python")  # True

# Comparison of booleans
print(True == False)  # False

# Comparison of integers
print(-5 * 15 != 75)  # True

# Comparison of strings
print('pyscript' == 'PyScript')  # False

# Compare a boolean with an integer
print(True == 1)  # True

# and/or/not operator ##################################################################
x = 8
y = 9
print(not (not (x < 3) and not (y > 14 or y > 10)))

# numpy Comparision #################################################################
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)  # [ True  True False False]

# my_house less than your_house
print(my_house < your_house)  # [False  True  True False]

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Logical #################################################################
area = 10.0
if (area < 9):
    print("small")
elif (area < 12):
    print("medium")
else:
    print("large")

# while loop #################################################################
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

# for loop ##################################################################
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for a in areas:
    print(a)

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    print("person " + str(index) + ": " + str(height))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for h in house:
    print("the " + str(h[0]) + " is " + str(h[1])+" sqm")

world = {"afghanistan": 30.55,
         "albania": 2.77,
         "algeria": 39.21}
print(world)
print(world.items())
print(world.keys())
print(world.values())

for key, value in world.items():
    print(key + " -- " + str(value))


# Loop over numpy array. If you're dealing with a 2D NumPy array, it's more complicated.
#  A 2D array is built up of multiple 1D arrays
# for x in np.nditer(my_array):

# Loop over DataFrame brics - Here lab has the columns and row has the data
# for lab, row in brics.iterrows()


# pandas - for loop ##################################################################
cars = pd.read_csv('datasets/cars.csv', index_col=0)

for val in cars:
    print(val)
# cars_per_cap
# country
# drives_right

# Adapt for loop
for lab, row in cars.iterrows():
    print(f"lab type is {type(lab)} and the row type is {type(row)}")
    print(lab + " : "+str(row['cars_per_cap']))

# Use .apply(str.upper)
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)

# This is without the for loop
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)


## Random nos#################################################################################
# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Generate and print random from 1,2,3,4,5,6
print(np.random.randint(1, 7))
