# 1) What is the output?

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
    
print(fun(0,3))

# answer --> 0

# 2) Which of the senteces are true about the following code (select two answers)?

nums = [1,2,3]
vals = nums

# a) nums has the same length as vals --> CORRECT
# b) nums and vals are different lists
# c) vals is longer than nums
# d) nums and vals are different names of the same lists --> CORRECT


# 3) How many hashes will be printed?
lst = [[x for x in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

# answer --> three


# 4) What is the result of the following division:
print(1//2) 
# answer --> 0

# 5) What is the output?
tup = (1,2,4,8)
tup = tup[-2:-1] # (4,8)
tup = tup[-1] # (4)
print(tup)
# answer --> 4

# 6) What is the operator able to check whether two values are not equal?
# answer --> !=

# 7) What is the output?
def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)
print(function_2(2))
# answer --> runtime error

# 8) The following code is correct?
def fun(a,b):
    return b ** a
# print(fun(b=2, 2))
# answer --> NO, the way the function is being called is incorrect

# 9) What is the output?
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
# answer --> 0 1

# 10) The meaning of a positional argument is determined by:
# a) its connection with existing variables
# b) its value
# c) the argument's name specified along with its value
# d) its position within the argument list ---> CORRECT

# 11) What is the output sending 3 and 6?

y = input() # "3"
x = input() # "6"
print(x + y) # "63"
# answer --> 63

# 12) what value will be assigned to the x variable?
z = 0
y = 10
x = (y < z and z > y) or (y > z and z < y)
# answer --> True

# 13) what is the output? ---> ????
my_list = [ x * x for x in range(5)] # [0, 1, 4, 9, 16]
print("aqui", my_list)
def fun(lst):
    del lst[lst[2]] # lst[2] == 4 | lst[lst[2]] == 16
    return lst
# answer --> # [0,1,4,9]


# 14) how many starts will be printed?
# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")
# answer --> the code will enter in an infinite loop

# 15) how many elements does the list contain?
lst = [i for i in range(-1, -2)]
# answer --> [] zero

# 16) What is the output?
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1], end="")
# answer --> 21

# 17) What is the expected result?
foo = (1,2,3)
foo.index(0) # ValueError: tuple.index(x): x not in tuple
# it will return a value error

# 18) what is the expected behavior?
try:
    print(5/0)
    # break
except:
    print("Sorry, something went wrong")
# except (ValueError, ZeroDivisionError):
    print("Too bad...")
# the code will return a syntax error because break is outside loop

# 19) What is the output?
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three'] # 'one'
# len(dct) == 3
for k in range(len(dct)):
    v = dct[v]
    # 1) 'two'
    # 2) 'three
    # 3) 'one'
print(v) #  three
# answer --> 'one'

# 20) What is the result?
x = 1
y = 2
x,y,z = x, x, y
z,y,z = x,y,z 
print(x,y,z)
# answer --> 1,1,2

# 21) what is the output if the user types 0? ???
try:
    value = input()
    print(int(value)/len(value))
except ValueError:
    print("Bad input")
except ZeroDivisionError:
    print("Very bad input")
except TypeError:
    print("very very bad input")
except:
    print("booo")
# answer --> 0.0

# 22) what is the output?
def fun(inp=2, out=3):
    return inp*out
print(fun(out=2)) 
# answer --> 3

# 23) Which of the following snippets shows the correct way of handling multiple exceptions in a single except clause?
# a) except (TypeError, ValueError, ZeroDivisionError)
# b) except (TypeError, ValueError, ZeroDivisionError): --> CORRECT
# c) except: TypeError, ValueError, ZeroDivisionError
# d) except TypeError, ValueError, ZeroDivisionError:

# 24) What is the output using 3 and 2?
x = int(input()) # 3
y = int(input()) # 2
x = x % y
x = x % y
y = y % x
print(y) 
# answer --> 0

# 25) What is the output using 2 and 4?
x = float(input()) # 2.0
y = float(input()) # 4.0
print(y ** (1/x))
# answer --> 2.0

# 26) What is the output?
x = 1 // 5 + 1 / 5
print(x)
# answer --> 0.2

# 27) What is the output?
dd = {"1": "0", "0": "1"}
# for x in dd.vals()
# answer --> the code is erroneous since there is no vals method

# 28) What will happen when you attempt to run the following code?
# print(Hello,World)
# answer --> it will raise the SyntaxError exception

# 29) Assuming that my_tuple is a correct created tuple, the following instruction is:
my_tuple = (1,2)
# my_tuple[1] = my_tuple[1] + my_tuple[0]
# answer --> illegal because tuples are immutable

# 30) What is the output?
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))
# answer --> 2

# 31) Which of the following lines correctly invoke the function defined below? (select two answers)
def fun(a,b,c=0):
    pass
# a) fun(b=0, a=0) --> CORRECT
# b) fun(b=1)
# c) fun() 
# d) fun(0,1,2) --> CORRECT

# 32) What is the output?
my_list= [1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list) 
# answer --> [1,1,1,2]

# 33) What is the output of the following piece of code?
print("a", "b", "c", sep="sep")
# answer --> asepbsepc

# 34) Take a look at the code and chose the true statement:
nums = [1,2,3]
vals = nums
del vals[:]
# a) nums is longer than vals
# b) nums and vals have the same length --> CORRECT
# c) vals is longer than nums
# d) the snipped will cause a runtime error

# 35) Which of the following variable names are illegal and will cause the SyntaxError? (select two answers)
# a) In
# b) print
# c) in --> THIS
# d) for -- THIS