import numpy as np
print('Hello World')

# Type Conversion##########################################################################################
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7
# Fix the printout
print("I started with $" + str(savings) +
      " and now have $" + str(result) + ". Awesome!")
# Definition of pi_string
pi_string = "3.1415926"
# Convert pi_string into float: pi_float
pi_float = float(pi_string)
# List##########################################################################################
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
# Print out the type of house
print(type(house))
print(house[0])
print(house[-1])
# deleting an element in the list############################################################

areas = ["hallway", 11.25, "kitchen", 18.0,
         "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

del (areas[-4:-2])
list
l = ['a', 'c', 'best', 'c', 'd']
print(l[1:3])
print(max(l))
print(len(l))
b = 'best'
print(len(l[1]))
print(l.index('best'))
print(l.count('c'))
l.append('e')
l.reverse()
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
# Print out full_sorted
print(full_sorted)
# Numpy###########################################################################################
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(type(baseball))  # <class 'list'>
print(type(np_baseball))  # <class 'numpy.ndarray'>
print(np_baseball)  # [180, 215, 210, 210, 188, 176, 209, 200]
# Numpy-Implementation##############################################################################
x = [1, 2, 3]
# y = x**2 # This is a Error
y = x*2
print(y)  # [1, 2, 3, 1, 2, 3]
np_y = np.array(x)
np_y_1 = np_y**2  # [1 4 9]
print(np_y_1)
np_y_2 = np_y * 2  # [2 4 6]
print(np_y_2)
x = [4, 9, 6, 3, 1]
print(x[1])  # 9
y = np.array(x)
print(y[1])  # 9
high = y > 5
print(y > 5)  # [False  True  True False False]
print(y[high])  # [9 6]
print(np.array([True, 1, 2]) + np.array([3, 4, False]))  # [4 5 2]
print(np.array([4, 3, 0]) + np.array([0, 2, 2]))  # [4 5 2]
# BMI calculation using numpy################################################################
height_in = [100, 200, 300]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)
print(type(np_height_in))  # <class 'numpy.ndarray>'
# Print out np_height_in
print(np_height_in)  # [100 200 300]
# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254
# Print np_height_m
print(np_height_m)  # [2.54 5.08 7.62]
weight_lb = [5, 6, 7]
# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592
# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2
# Print out bmi
print(bmi)  # [0.3515345  0.10546035 0.05468314]
# Create the light array
light = bmi < 0.1
# Print out light
print(light)  # [False False  True]
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])  # [0.05468314]
print(np_height_in[1:3])  # [200 300] this is the subset
# ############################################################################################
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# print(baseball[2, 0])  # Error
print(baseball[2][0])  # 210
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(np_baseball)
# [[180.   78.4]
#  [215.  102.7]
#  [210.   98.5]
#  [188.   75.2]]
# Print out the type of np_baseball
print(type(np_baseball))  # <class 'numpy.ndarray'>
# Print out the shape of np_baseball
print(np_baseball.shape)  # (4, 2) gives the no.of rows and no.of columns
# Print out the 2nd row of np_baseball
print(np_baseball[1, :])  # [215.  102.7]
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)  # [ 78.4 102.7  98.5  75.2]
# Print out height of 3rd player
print(np_baseball[2, 0])  # 210.0
print(np_baseball[2][0])  # 210.0
print(np_baseball[:, 0:1])
# [[180.]
#  [215.]
#  [210.]
#  [188.]]
print(np_baseball[1:3, :])
# [[215.  102.7]
#  [210.   98.5]]
print(np_baseball[1:3, 0:1])
# [[215.]
#  [210.]]
# Mean,Median,standard deviation,corelation,###########################################################
np_mat = np.array([[1, 2, 11],
                   [3, 4, 12],
                   [5, 6, 13]])

print(np_mat[:, 0])  # [1 3 5]

corr = np.corrcoef(np_mat[:, 0], np_mat[:, 1])  # corelation function
print(corr)
# [[1. 1.]
#  [1. 1.]]
print(np_mat * 2)
print(np_mat + np.array([10, 10, 10]))
print(np_mat + np_mat)

x = [1, 4, 8, 10, 12]
print("the mean of the data is {0} and the median is {1}".format(
    np.mean(x), np.median(x)))  # the mean of the data is 7.0 and the median is 8.0
# the mean of the data is 7.0 and the median is 8.0
print(f"the mean of the data is {np.mean(x)} and the median is {np.median(x)}")

avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))  # Average: 198.25

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))  # Median: 199.0

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
# Standard Deviation: 14.635146053251399
print("Standard Deviation: " + str(stddev))

print(np.sum(x))  # 35
print(np.sort(x))  # [ 1  4  8 10 12]
data = np.round(np.random.normal(10, 100, 10), 2)
print(data)  # it generates random 10 gaussian no, and rounds each no to 2 decimals
############################################################################################
positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

print(np_positions == 'GK')  # [ True False False False]
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
# Median height of goalkeepers: 191.0

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
# Median height of other players: 184.0
