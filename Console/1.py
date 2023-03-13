print('Hello World')
import numpy as np

# ############################################################################################
# # baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# # np_baseball = np.array(baseball)
# # print(type(baseball))  #<class 'list'>
# # print(type(np_baseball)) #<class 'numpy.ndarray'>
# # print(np_baseball) #[180, 215, 210, 210, 188, 176, 209, 200]
# ############################################################################################
# # x= [1,2,3]
# # # y = x**2 # This is a Error
# # y = x*2
# # print(y) #[1, 2, 3, 1, 2, 3]
# # np_y = np.array(x)
# # np_y_1 = np_y**2  #[1 4 9]
# # print(np_y_1)
# # np_y_2 = np_y *2  #[2 4 6]
# # print(np_y_2)
# ############################################################################################
# # height_in = [100,200,300]
# # # Create a numpy array from height_in: np_height_in
# # np_height_in = np.array(height_in)
# # # Print out np_height_in
# # print(np_height_in)
# # # Convert np_height_in to m: np_height_m
# # np_height_m = np_height_in *0.0254
# # # Print np_height_m
# # print(np_height_m)
# # weight_lb = [5,6,7]
# # # Create array from weight_lb with metric units: np_weight_kg
# # np_weight_kg = np.array(weight_lb) * 0.453592
# # # Calculate the BMI: bmi
# # bmi = np_weight_kg / np_height_m ** 2
# # # Print out bmi
# # print(bmi)
# # # Create the light array
# # light = bmi < 0.1
# # # Print out light
# # print(light)
# # # Print out BMIs of all baseball players whose BMI is below 21
# print(bmi[light])
# ############################################################################################
# # x = [4 , 9 , 6, 3, 1]
# # print(x[1])
# # y = np.array(x)
# # print(y[1])
# # high = y > 5
# # print(y[high])
# # print(np.array([True, 1, 2]) + np.array([3, 4, False]))
# # print(np.array([4, 3, 0]) + np.array([0, 2, 2]))

# # print(np_height_in[100:111])
# ############################################################################################
# # Create baseball, a list of lists
# # baseball = [[180, 78.4],
# #             [215, 102.7],
# #             [210, 98.5],
# #             [188, 75.2]]
# # # Create a 2D numpy array from baseball: np_baseball
# # np_baseball = np.array(baseball)
# # print(np_baseball)
# # # Print out the type of np_baseball
# # print(type(np_baseball))
# # # Print out the shape of np_baseball
# # print(np_baseball.shape)
# ############################################################################################
# # np_baseball = np.array(baseball)
# # print(np_baseball)
# # # Print out the 50th row of np_baseball
# # print(np_baseball[49,:])
# # # Select the entire second column of np_baseball: np_weight_lb
# # np_weight_lb = np_baseball[:,1]
# # # Print out height of 124th player
# # print(np_baseball[123,0])
# ############################################################################################
# # np_mat = np.array([[1, 2,11],
# #                    [3, 4,12],
# #                    [5, 6,13]])

# # print(np_mat[:,0])

# # corr = np.corrcoef(np_mat[:,0],np_mat[:,1])
# # print(corr)
# # print(np_mat * 2)
# # print(np_mat + np.array([10, 10]))
# # print(np_mat + np_mat)
# ############################################################################################
# # x = [1, 4, 8, 10, 12]
# # print(np.mean(x))
# # print(np.median(x))

# # avg = np.mean(np_baseball[:,0])
# # print("Average: " + str(avg))

# # # Print median height. Replace 'None'
# # med = np.median(np_baseball[:,0])
# # print("Median: " + str(med))

# # # Print out the standard deviation on height. Replace 'None'
# # stddev =  np.std(np_baseball[:,0])
# # print("Standard Deviation: " + str(stddev))

# positions = ['GK', 'M', 'A', 'D']
# heights = [191, 184, 185, 180]

# # Convert positions and heights to numpy arrays: np_positions, np_heights
# np_positions = np.array(positions)
# np_heights = np.array(heights)

# # Heights of the goalkeepers: gk_heights
# gk_heights = np_heights[np_positions == 'GK']

# # Heights of the other players: other_heights
# other_heights = np_heights[np_positions != 'GK']

# # Print out the median height of goalkeepers. Replace 'None'
# print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# # Print out the median height of other players. Replace 'None'
# print("Median height of other players: " + str(np.median(other_heights)))