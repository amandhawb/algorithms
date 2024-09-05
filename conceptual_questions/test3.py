# 1) in python a function definition:
# a) must be placed before the first invocation --> TRUE
# b) may be placed anywhere inside the code after the first invocation
# c) cannot be placed among other code

# 2) in python a function parameter is a kind of variable accessible:
# a) only inside the function --> TRUE
# b) only after the function definition's completion
# c) anywhere in the code

# 3) a way of passing arguments in which the order of the arguments determines the
# initial parameter's values is referred to as:
# a) sequencial
# b) positional --> TRUE
# c) ordered

# 4) in python a variable defined outside a function:
# a) may be freely accessed inside the function
# b) may not be accessed in any way inside the function
# c) may be read, but not written (something more is needed to do so) --> TRUE

# 5) if a list is passed into a function as an argument, deleting any of its elements inside the function using the del instruction:
# a) will not affect the argument
# b) will affect the argument --> TRUE
# c) will cause an runtime error


# 6) 
# def fun(in=2, out=3):
#     return in * out

# print(fun(3))


# 7) What is the output of the following code?
tup = (1, ) + (1, )
tup = tup + tup
print(len(tup)) # 4


# 8) What is the output of the following program if the user enters 'kangaroo' at the first prompt and '0' at the second prompt?

try:
    first_prompt = input('Enter the first value: ')
    a = len(first_prompt)
    second_prompt = input('Enter the second value: ')
    b = len(second_prompt) * 2
    print(a/b)
except ZeroDivisionError:
    print('Do not divide by zero!')
except ValueError:
    print('Wrong value')
except:
    print('Error.Error.Error')

# answer --> 4.0


# 9) What is the expected behavior of the following program if the user enters '0'?
value = input('Enter a value: ')
print(10/value)

# answer --> The program will raise the TypeError exception