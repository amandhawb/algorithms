# 1) Arrange the code to form a conditional instruction which guarantees that a certain statement is executed when the places_occupied variable is greater than 0
# ANSWER --> if places_occupied > 0:

# 2) Arrange the code to form a conditional instruction which guarantees that a certain statement is executed when the discount variable is less or equal to than 15.0
# ANSWER --> if discount <= 15.0:

# 3) What is the output of the following code?
planets = 1 + 1 // 2 * 3 # 1
if planets > 0:
    print("#")
elif planets > 1:
    print("##")
else:
    print("###")
# ANSWER --> "#"

# 4) What is the output of the following code?
planets = 4 - 3 // 2 + -1 # 2 
if planets < 0:
    print("#")
elif planets >= 2:
    print("##")
else:
    print("###")
# ANSWER --> "##"

# 5) Write an algorithm to obtain a code which outputs ##
shift = 1 + 2 * 3 # 7
if shift < 0:
    print("#")
elif shift > 2:
    print("##")
else:
    print("###")

# 6) Write an algorithm to obtain a code which outputs #
shift = 3 // 2 - 2 # -1
if shift <= 0:
    print("#")
elif shift >= 2:
    print("##")
else:
    print("###")  

# 7) How many asterisks does the following code output?
torque = 5
while torque > 0:
    torque -= 3
    print("*", end="")
else:
    print("*")
# ANSWER --> 3

# 8) How many asterisks does the following code output?
torque = 1
while torque > 2:
    torque *= 2
    print("*", end="")
else:
    print("*")
# ANSWER --> 2

# 9) What happens when the user runs the following code?
power = 1
while power != 10:
    power *= 2
    if power == 5:
        continue
    print("@", end="")
else:
    print("@")
# ANSWER --> The program enters an infinite loop because the condition (power != 10) never met

# 10) What happens when the user runs the following code?
power = 1
while power < 5:
    power += 1
    print("@", end="")
    if power == 3:
        break
else:
    print("@")
# ANSWER --> The program outputs two at signs (@@) to the screen

# 11) Arrange the code to obtain a loop which executes its body with the step variable going through the values 0, 2, and 4 (in that order)
# ANSWER --> for step in range(0, 5, 2):

# 12) Arrange the code to obtain a loop which executes its body with the step level going through the values 5, 4, and 3 (in that order)
# ANSWER --> for level in range(5, 2, -1):

# 13) What happens when the user runs the following code?
angle = 0
for i in range(5):
    if i % 2 == 1:
        angle += 1
else:
    angle -= 1
print(angle)
# ANSWER --> The code outputs 1

# 14) What happens when the user runs the following code?
angle = 1
for i in range(2, 5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1
print(angle)
# ANSWER --> The code outputs 2

# 15) What is the expected output of the following code?
others = 0
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1
print(others)
# ANSWER --> 3

# 16) What is the expected output of the following code?
others = -1
for i in range(1, 3):
    for j in range(1, 2):
        if i == j:
            others += 1
    else:
        others += 1
print(others)
# ANSWER --> 2
