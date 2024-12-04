# Basic Exception Handling
# Write a program to divide two numbers provided by the user. Handle the following exceptions:
# Division by zero (ZeroDivisionError)
# Invalid input (ValueError)

def divide_numbers():
    try:
        num1 = int(input("Enter numeretor: "))
        num2 = int(input("Enter denominator: "))

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        
        return num1 / num2
    
    except ValueError:
        print("Invalid Input. Please enter valid numbers")
        return None
    
    except ZeroDivisionError as e:
        print(e)
        return None

result = divide_numbers()
if result is not None:
    print(f"Result: {result}")
    
# Raise an Exception
# Create a program that asks the user to enter their age. If the user enters a negative age, raise a ValueError with the message: "Age cannot be negative."

def age_checker(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return f"Age {age} is valid."
try:
    print(age_checker(-1))
except ValueError as e:
    print(e)


# Using else and finally
# Write a program to open a file named example.txt for reading.
# If the file doesn't exist, catch the FileNotFoundError.
# Use else to print the file's content.
# Use finally to print "Operation completed."

def read_file():
    try:
        f = open("example.txt")
    except FileNotFoundError:
        print("File Not Found!")
    else:
        print(f)
    finally:
        print("Operation completed.")

read_file()


# Assertion Test
# Write a program that takes a list of numbers and asserts that all numbers are positive. If the assertion fails, raise an error with the message: "List contains negative numbers."
def check_list(nums):
    for num in nums:
        assert num >= 0, "List contains negative numbers."

try:
    print(check_list([1,2,3,-1]))
except AssertionError as e:
    print(e)
