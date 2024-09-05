# 1) a function defined in the following way (select two answers):

def function(x=0):
    return x

# a) may be invoked without any argument --> TRUE
# b) must be invoked with exactly one argument
# c) may be invoked with exactly one argument --> TRUE
# d) must be invoked without any argument

# 2) What is the output of the following code:

tup = (1, 2, 4, 8)
tup = tup[1:-1] # 2, 4 (tup is sliced from index 1 to -1. In Python, slicing a tuple with tup[start:stop] extracts a new tuple starting from index start up to (but not including) index stop)
tup = tup[0] # 2
print(tup)

# 3) Assuming that my_tuple is a correctly created tuple, the fact that tuples are immutable means that the following instruction:
my_tuple = (1,2)
my_tuple[1] = my_tuple[1] + my_tuple[0]
print(my_tuple)
# a) can be executed if and only if the tuple contains at least two elements
# b) is illegal --> TRUE
# c) is fully correct
# d) may be illegal if the tuple contains strings

# 4) What is the output?
def fun(x, y, z):
    return x + 2 * y + 3 * z

print(fun(0, z=1, y=3)) # 9

# 5) What code would you insert instead of the comment to obtain the expected output?
# Expected output: 
# a
# b
# c
dictionary = {}
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list) -1):
    dictionary[my_list[i]] = (my_list[i], )
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # code here

# a) print(k[0]) --> TRUE
# b) print(k)
# c) print(k["0"])
# d) print(k['0'])

# 6) Which of the following lines properly starts a function using two parameters, both with zeroed default values?
# a) fun fun(a=0, b):
# b) def fun (a=b=0):
# c) fun fun (a, b=0):
# d) def fun (a=0, b=0): --> TRUE

# 7) The following snippet:
def func(a,b):
    return a ** a
print(func(2))
# a) will output 4
# b) is erroneous --> TRUE
# c) will output 2
# d) will return None

# 8) Select the true statements about the try-except block in relation to the following example. (Select two answers.)
try:
    pass
    # Some code is here...
except:
    pass
    # Some code is here...

# a) If you suspect that a snippet may raise an exception, you should place it in the try block. --> TRUE
# b) The code that follows the except statement will be executed if the code in the try clause runs into an error. --> TRUE
# c) The code that follows the try statement will be executed if the code in the except clause runs into an error.
# d) If there is a syntax error in code located in the try block, the except branch will not handle it, and a SyntaxError exception will be raised instead.

# 9) What is the output?
try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input")
except ZeroDivisionError:
    print("Very bad input")
except TypeError:
    print("Very very bad input")
except:
    print("Boo")

# answer --> "Very very bad input"

# 10) What is the output?
def f(x):
    if x == 0:
        return 0
    return x + f(x-1)
print(f(3))

# answer --> 6

# 11) Which one of the following lines properly starts a parameterless function definition?
# a) def fun:
# b) fun function ():
# c) def fun (): --> TRUE
# d) function fun ():

# 12) What is the output?
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 
    
# print(fun(fun(2)) + 1) # RUNTIME ERROR

# 13) What is the output?
def func_1(a):
    return a ** a
def func_2(a):
    return func_1(a) * func_1(a)
print(func_2(2))

# answer --> 16

# 14) What is the output?
def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))
# answer --> 4

# 15) Which of the following statements are true? (Select two answers)
# a) The None value cannot be used outside functions
# b) The None value can be assigned to variables --> TRUE
# c) The None value can be compared with variables --> TRUE
# d) The None value can be used as an argument of arithmetic operators

# 16) What is the output?
def fun(x):
    x += 1
    return x
x = 2
x = fun(x + 1)
print(x)
# answer --> 4

# 17) What is the output?
def fun(x):
    global y
    y = x * x
    return y
fun(2)
print(y)
# answer --> 4

# 18) What is the output?
def any():
    print(var + 1, end='')
var = 1
any()
print(var)
# answer --> 21

# 19) What is the output?
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one'] # v = 'two'
for k in range(len(dictionary)):
    v = dictionary[v]
    # first iteration - v = 'three'
    # second iteration - v = 'one'
    # third iteration - v = 'two' 
print(v)
# answer --> two

# 20) A built-in function is a function which:
# a) has been placed within your code by another programmer
# b) has to be imported before use
# c) comes with Python, and is an integral part of Python --> TRUE
# d) is hidden from programmers

# 21) The fact that tuples belong to sequence types means that:
# a) they can be extended using the .append () method
# b) they can be indexed and sliced like lists --> TRUE
# c) they can be modified using the del instruction
# d) they are actually lists

# 22) What is the output of the following snippet?
my_list = ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3] # ['Mary', 'had', 'a', 'lamb']
    my_list[3] = 'ram' # ['Mary', 'had', 'a', 'ram']
print(my_list(my_list))

# answer --> TYPE ERROR: 'function'object does not support item deletion