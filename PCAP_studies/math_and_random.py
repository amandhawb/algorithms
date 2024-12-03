# Math Module:
# Square Root & Factorial
# Calculate the square root of 121, the factorial of 6, and the floor and ceiling of 3.6.
from math import sqrt, factorial, floor, ceil
print(sqrt(121))
print(factorial(6))
print(floor(3.6))
print(ceil(3.6))

# Hypotenuse Calculation
# Use math.hypot() to calculate the hypotenuse of a right triangle with sides 9 and 12.
from math import hypot
print(hypot(9, 12))

# Math Constants
# Print the value of math.pi and math.e to approximate pi and Euler’s number.
import math
print(math.pi)
print(math.e)

# Trigonometric Functions
# Use math.radians() to convert 30 degrees to radians, then use math.sin() to find its sine.
result = math.radians(30)
print(math.sin(result))


# Random Module:
# Random Number Generation
# Generate 5 random numbers between 1 and 50 using random.randint().
import random
print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))

# Random Selection
# From a list of colors ["red", "green", "blue", "yellow"], randomly choose one using random.choice().
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))

# Shuffling a List
# Create a list of numbers from 1 to 10. Shuffle the list using random.shuffle() and print the result.
nums = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(nums)
print(nums)

# Random Sampling
# Generate a random sample of 3 numbers from a range of 1 to 20 (without replacement) using random.sample().
print(random.sample(range(1,20), 3))
