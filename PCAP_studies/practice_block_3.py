# 1) Assuming that the following assignment has been successfully executed, select the expressions which will NOT raise any exception. (Select two expressions)
numbers = [4,3,2,1]
# a) numbers[numbers[0]]
# b) numbers[3:5] --> CORRECT
# c) numbers[4]
# d) numbers[numbers[3]] --> CORRECT

# 2) Assuming that the following assignment has been successfully executed, select the expressions which will NOT raise any exception. (Select two expressions)
numbers = [2,3,5,8]
# a) numbers[-numbers[3]] # -8
# b) numbers[3:3] --> CORRECT
# c) numbers[numbers[1]] # 8
# d) numbers[numbers[3]]

# 3) Assuming that the following assignment has been successfully executed, which of the following expressions evaluate to False? (Select two expressions)
the_data = [0, .0, True]
# a) 0.0 in the_data
# b) the_data.index(True) == 0 --> CORRECT (returns False)
# c) len(sorted(the_data)) == len(the_data)
# d) len(the_data) == the_data[0] --> CORRECT (returns False)

# 4) Assuming that the following assignment has been successfully executed, which of the following expressions evaluate to True? (Select two expressions)
the_data = ['data', -1, 2.718281]
# a) int(the_data[2]) == len(the_data)
# b) the_data.index(-1) > 0 --> CORRECT (returns True)
# c) the_data[1] not in the_data
# d) 'data' in the_data --> CORRECT (returns True)

# 5) What is the expected output of the following code?
list_one = [1,2]
list_two = list_one
list_two.append(3)
print(list_one[-1])
# ANSWER --> 3

# 6) What is the expected output of the following code?
list_one = [1,2]
list_two = list_one[:]
list_two.append(3)
print(list_one[-1])
# ANSWER --> 2

# 7) What is true about tuples? (Select two answers)
# a) The del keyword can be applied to a single tuple element in order to remove it
# b) Tuples are immutable, which menas that you're not allowed to change their contents --> CORRECT
# c) You can use indexing in order to get ant tuple's element --> CORRECT
# d) The .append() method can be used to extend any tupple

# 8) What is true about tuples? (Select two answers)
# a) All tuple elements must be of the same type
# b) The phrase (1) describes a one-element tuple
# c) The phrase tuple() can be used to produce an empty tuple --> CORRECT
# d) The + operator can be applied to tuples and means concatenation --> CORRECT

# 9) What is the expected result of the following code?
answers = (True, True, False)
selection = answers[3:]
points = 0
for answer in selection[-2:]:
    if answer:
        points += 1
print(points)
# ANSWER --> 0

# 10) What is the expected result of the following code?
answers = (True, False, True)
selection = answers[2:]
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)
# ANSWER --> 1

# 11) Assuming that a Pepperoni Pizza costs $2.99, create a valid line of code, which makes a relevant pizzaria's menu entry within the pizza_menu dictionary ("Pepperoni Pizza" is the key).
pizza_menu = {"Pepperoni Pizza" : 2.99 }

# 12) Assuming that the pizza_menu contains pizza:price pairs, create a valid line of code which retrieves the Margherita Pizza price, and assigns it to the charge variable
charge = pizza_menu["Margherita Pizza"]

# 13) What is the exected output of the following code?
train_speed = {"FlyingScotsman": 201, "TGV": 320, "Shinkansen": 320}
for train in train_speed:
    print(train[0], end="")
# ANSWER --> FTS

# 14) What is the exected output of the following code?
train_speed = {"FlyingScotsman": 201, "TGV": 320, "Shinkansen": 320}
for train in train_speed.values():
    print(str(train)[0], end="")
# ANSWER --> 233