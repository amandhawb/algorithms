# 1) Which of the following snippets correctly define a function? (Select two answers)
# a) def do_not_touch:
#        parameter *= 1
# b) def 0_effects(parameter):
#        return parameter + 1
# c) def do_eval(parameter): --> CORRECT
#        variable = parameter
#        return variable
# d) def no_operation(parameter): --> CORRECT
#        return parameter

# 2) A user-defined function is invocked twice in the following line of code. What do you call the argument passing techniques which have been used here?
result = function(function(parameter=0))
# a) positional --> CORRECT the outer function uses this technique
# b) keyword --> CORRECT the inner function uses this technique (parameter = 0)
# c) indicatory
# d) reference

# 3) What is the expected result of the following code?
def sample(value):
    return value + value
x = sample(value = 1)
y = sample(x)
print(y)
# ANSWER --> 4

# 4) What is the expected result of the following code?
def sample(value):
    return total + value
total = 0
new_total = sample()
new_total = sample(total)
print(total)
# ANSWER --> error, line 31 is wrong because the function sample expects one argument

# 5) Which of the following functions CANNOT be invoked with one argument?
# a) def one(level=100):
#       pass
# b) def two(level):
#       pass
# c) def four(): --> CORRECT. This function can't have one argument
#       pass
# a) def three(level, size=0):
#       pass

# 6) Which of the following functions CAN be invoked with one argument?
# a) def three(v1, v2, v3=0):
#       pass
# b) def four():
#       pass
# c) def one(zero = 0): --> CORRECT. This function can have one argument
#       pass
# a) def two(first, second):
#       pass

# 7) What is the expected result of the following code?
def process(data):
    data = [1,2,3]
    return data[-2]
measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])
# ANSWER --> 0

# 8) What is the expected result of the following code?
def process(data):
    data[1] = 2
    return data[-2]
measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])
# ANSWER --> 2

# 9) What is the expected result of the following code?
def combine(width, height=10, depth=0, is_3D=False):
    return [is_3D, width, height, depth]
print(combine(height=1, width=2)[3])
# ANSWER --> 0

# 10) What is the expected result of the following code?
def combine(width, height=2, depth=0, is_3D=False):
    return [is_3D, width, height, depth]
print(combine(1)[2])
# ANSWER --> 2

# 11) What is the expected result of the following code?
def walk(stop, start=1):
    print(start, end=" ")
    if start + 1 < stop:
        walk(stop, start+1)
walk(3)
# ANSWER --> 1 2

# 12) What is the expected result of the following code?
def walk(top):
    if top == 0:
        return 0
    return top + walk(top-1)
print(walk(2))
# ANSWER --> 3

# 13) What is true about exceptions in Python? (Select two answers)
# a) IndexError may be raised when you try to access a nonexistent list element --> TRUE
# b) Slicing a list can raise an exception
# c) IndexError may be raised when you try to access a nonexistent dictionary key
# d) An unhandled exception causes the program to terminate --> CORRECT 

# 14) What is false about exceptions in Python? (Select two answers)
# a) More than one except branch can be executed when an exception is raised --> CORRECT (it is false)
# b) If any of the raised exceptions remains unhandled, program execution is terminated and an error message is printed
# c) The code put inside the try branch may not be fully executed
# d) Any code put inside the try branch is always fully executed --> CORRECT (it is false)

# 15) Drag and drop the boxes in order to build a program which prints Mishit to the screen
try:
    character = "ABC"[3]
except IndexError:
    print("Mishit")
except:
    print("Failure")
    
# 16) Drag and drop the boxes in order to build a program which prints Not a number to the screen
try:
    width = float('width')
except ValueError:
    print("Not a number")
except:
    print("Bad luck")