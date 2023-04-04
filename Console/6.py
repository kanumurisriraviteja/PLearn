# ErrorHandling,Iterator,enumerator,zip,chuncks

import pandas as pd

# Exception Handling#########################################################################
# Define shout_echo


def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
        exclamation marks at the end of the string."""
    try:
        # Raise an error with raise
        if echo < 0:
            raise ValueError('echo must be greater than or equal to 0')

        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_word
        shout_word = echo_word + '!!!'

        # Return shout_word
        return shout_word
    except:
        print('exception has occured')


# Call shout_echo
# particleparticleparticleparticleparticleparticle!!!
print(shout_echo("particle", echo=6))

# exception has occured
# None
print(shout_echo("particle", echo=-6))

# Iterator################################################################################
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for item in flash:
    print(item)

# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))  # jay garrick
print(next(superhero))  # barry allen

print(superhero)  # <list_iterator object at 0x000001B9D6C45450>
print(*superhero)  # wally west bart allen >> gets all the elements in a sinle shot

# Create an iterator for range(3): small_value
small_value = iter(range(5))

# Print the values in small_value
print(next(small_value))  # 0
print(next(small_value))  # 1


# Loop over range(3) and print the values
for item in small_value:
    print(item)
# 2
# 3
# 4

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))  # 0
print(next(googol))  # 1
print(next(googol))  # 2
print(next(googol))  # 3
print(next(googol))  # 4


# Enumerator################################################################
# Create a list of strings: mutants
mutants = ['charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = enumerate(mutants)

# Print the list of tuples
print(mutant_list)  # <enumerate object at 0x0000015DEBA22700>

# Create a list of tuples: mutant_list
mutant_list_1 = list(enumerate((mutants)))
# Print the list of tuples
# [(0, 'charles xavier'), (1, 'bobby drake'), (2, 'kurt wagner'), (3, 'max eisenhardt'), (4, 'kitty pryde')]
print(mutant_list_1)


# Unpack and print the tuple pairs
for index1, value1 in mutant_list:
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

# ZIP/unzip#########################################################################

mutants = ['a', 'b']
aliases = ['c', 'd']
powers = ['e', 'f']


# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))
# Print the list of tuples
print(mutant_data)  # [('a', 'c', 'e'), ('b', 'd', 'f')]


# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)  # <zip object at 0x000001EE8383F740>
print(zip(mutants, aliases, powers))  # <zip object at 0x000001EE8383F740>

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
# a c e
# b d f

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)  # ('a', 'e') ('b', 'f')

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
print(f"{result1} {type(result1)}")  # ('a', 'b') <class 'tuple'>
print(result2)  # ('e', 'f')
print(f"{mutants} {type(mutants)}")  # ['a', 'b'] <class 'list'>
print(powers)  # ['e', 'f']

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)  # False
print(result2 == powers)  # False

# iterating over the chuncks###################################################
# Define count_entries()


def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


# Call count_entries(): result_counts
result_counts = count_entries('datasets/tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)  # {'en': 97, 'et': 1, 'und': 2}
