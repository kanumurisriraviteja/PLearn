# NumPy is imported, seed is set
import numpy as np
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Scenario -1 : Run 100 times and plot the random walk ################################################
# Initialize random_walk
random_walk = [0]

for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# Scenario -2 : Run 250 time the same, 100 times and plot the random walk ################################################

# Simulate random walk 250 times
all_walks = []
for i in range(250):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# print(all_walks)
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]  # This step has all the last present value for the 250 runs

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
