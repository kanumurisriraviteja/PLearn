# fuctions local/global/nonlocal variables,inner,function pointer,*args,**kwargs,lamba - map,filter,reduce
from functools import reduce

# functions variables local and global###################################################
num = 5


def func1():
    num = 3
    print(num)  # 3 local scope


def func2():
    global num
    double_num = num * 2
    num = 6
    print(num)  # 6
    print(double_num)  # 10


func1()
func2()
print(num)  # 6

# Inner functions###################################################
# Define three_shouts


def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))


# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))  # ('a!!!', 'b!!!', 'c!!!')


# functional pointer###################################################
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo


# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))  # hellohello hellohellohello

# nonlocal scope###################################################
# Define echo_shout()


def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word * 2
    v1 = 5

    # Print echo_word
    print(echo_word)  # hellohello
    print(v1)  # 5

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word

        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
        print(echo_word)  # hellohello!!!
        v1 = 6
        print(v1)  # 6

    # Call function shout()
    shout()

    # Print echo_word
    print(echo_word)  # hellohello!!!
    print(v1)  # 5


# Call function echo_shout() with argument 'hello'
echo_shout('hello')

# *args###################################################
# Define gibberish


def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge


# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)  # luke
print(many_words)  # lukeleiahanobidarth

# **kwargs###################################################
# Define report_status


def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")


# First call to report_status()
report_status(name='luke', affiliation='jedi', status='missing')
# name: luke
# affiliation: jedi
# status: missing

# Second call to report_status()
report_status(name='anakin', affiliation='sith lord', status='deceased')
# name: anakin
# affiliation: sith lord
# status: deceased

# lambda###################################################


def echo_word(word1, echo): return word1 * echo
# Define echo_word as a lambda function: echo_word
# #echo_word = lambda word1, echo: word1 * echo


# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)  # heyheyheyheyhey

nums = [2, 4, 6, 8, 10]
result = map(lambda a: a ** 2, nums)
print(nums)  # [2, 4, 6, 8, 10]
print(list(result))

# lambda - map###################################################
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda a: a + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
# ['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']
print(shout_spells_list)

# lambda -filter###################################################
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin',
              'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda a: len(a) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)  # ['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']


# lambda - reduce###################################################
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1+item2, stark)

# Print the result
print(result)  # robbsansaaryabrandonrickon
