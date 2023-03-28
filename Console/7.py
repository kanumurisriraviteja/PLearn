# List comprehensions###################################################
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
result = [doc[0] for doc in doctor]
print(result)

# Create list comprehension: squares
squares = [i**2 for i in range(0, 10)]
print(squares)

# Creating a matrix of 5 * 5 ###################################################
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

# Comprehensions- list,dictionary with conditions###################################################
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if (len(member) >= 7)]

# Print the new list
print(new_fellowship)

# Create list comprehension: new_fellowship
new_fellowship = [member if (len(member) >= 7)
                  else '' for member in fellowship]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)


# Generators
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)
print(next(lengths))
# Iterate over and print the values in lengths
for value in lengths:
    print(value)


# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths


def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)


# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
