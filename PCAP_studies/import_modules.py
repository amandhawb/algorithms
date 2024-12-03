# Problem 1: Using Basic Import
# Write a program that:

# Imports the math module.
# Calculates and prints:
# The square root of 25.
# The ceiling and floor values of 4.7.
# The factorial of 5.

import math
print(math.sqrt(25))
print(math.ceil(4.7))
print(math.floor(4.7))
print(math.factorial(5))


# Problem 2: Specific Import
# Import only the sqrt and pow functions from the math module.
# Calculate the square root of 49 and raise 3 to the power of 4.
# Print the results.

from math import sqrt, pow
result1 = sqrt(49)
result2 = pow(3, 4)
print(result1)
print(result2)


# Problem 3: Using dir()
# Import the random module.
# Use dir(random) to list all the functions and attributes.
# Print the first 5 items from the list.

import random
result = dir(random)
print(result[0:5])


# Problem 4: Custom Module Path
# Create a Python file named greetings.py in a separate folder with the following code:
# def say_hello():
#     return "Hello, World!"
# Write a program to:
# Add the folder containing greetings.py to sys.path.
# Import the say_hello function and call it.
import sys
sys.path.append('/Users/amandhabarok/Workspace/Algorithms/my_modules')
from greetings import say_hello
print(say_hello())


# Problem 5: Exploring sys.path
# Print all the default directories in sys.path.
# Add a new directory path (temporary) and confirm it is added.
# Verify by printing sys.path again.
print(sys.path)
sys.path.append('temporary')
print(sys.path)


# Problem 6: Import Alias
# Import the random module as rnd.
# Use the rnd.randint(1, 100) function to generate and print a random number between 1 and 100.
import random as rnd
print(rnd.randint(1,100))


# Problem 7: Combining Concepts
# Import the platform module.
# Write a program to:
# Print the current platform name and version.
# Check the Python version using sys and platform.
import platform, sys
print(platform.version())
print(sys.platform)