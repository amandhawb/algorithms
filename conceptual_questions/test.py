# 1) how many stars the following code will print?
i = 2
while i >= 0:
    print('*')
    i -=2 
# answer --> 2


# 2) how many hashes will be printed?
for i in range(-1, 1):
    print('#')
# answer --> 2


# 3) what value will be assigned to the x variable?
z = 10
y = 0
x = z > y or z == y
# answer --> True


# 3) what is the output of the following code?
my_list = [3,1,-1]
my_list[-1] = my_list[-2]
# Python allows negative indexing, where:
# -1: Refers to the last element (-1)
# -2: Refers to the second-to-last element (1)

# answer --> [3,1,1]

# 5) the second assignment:
vals = [0,1,2]
vals[0], vals[1] = vals[1], vals[2]

# answer --> does not change the list's length

# 6) Take a look in the code below and choose one of the following statemens which is true:
nums = []
valss = nums
valss.append(1)
# a) valss is longer than nums
# b) nums is longer than valls
# c) nums and valss are of the same length --> TRUE

# 7) Take a look in the code below and choose one of the following statemens which is true:
numss = []
valsss = nums[:]
valsss.append(1)
# When you create valsss using the syntax valsss = numss[:], 
# you're creating a new list that is a shallow copy of numss. 
# This means that valsss is a separate list in memory, independent of numss. 

# a) valsss is longer than numss --> TRUE
# b) numss is longer than vallss
# c) numss and valsss are of the same length 

# 8) How many elements does the my_list contain?
my_list = [0 for i in range(1,3)]
# answer: 2

# 9) What is the output of the following snipped?
my_list2 = [0,1,2,3]
x = 1
for elem in my_list2:
    x *= elem
print(x)
# answer: 0