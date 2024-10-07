# 1) 
i = 0
while i <= 3:
    i += 2
    print('*')

# 2)
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print('#')

# 3)
var = 1
while var < 10:
    print("/")
    var = var << 1

# 4)
my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v]) 
# [1,1,1,1,2,3]
print(my_list)

# 5)
vals = [0,1,2]
vals.insert(0,1) # [1,0,1,2]
del vals[1] # [1,1,2]
# sum = 4

# 6)
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e)

# 7)
my_list2 = [[0,1,2,3] for i in range(2)]
# print(my_list2[2][0])
# [[0,1,2,3]
#  [0,1,2,3]]

# 8)
x = 1
x = x == x
print(x) # True

# 9)
numss = [1,2,3]
valss = numss
del valss[1:2] # [1,3]
print(valss)

# 10)
my_list_3 = [1,2,3]
my_list_4 = []
for v in my_list_3:
    my_list_4.insert(0, v) # [3,2,1]
print(my_list_4)

# 11)
for i in range(1):
    print('#')
else:
    print('#')

# 12) ??
my_list_5 = [3,1,-2]
print(my_list_5[my_list_5[-1]]) # 

# 13) ??
my_list_6 = [1,2,3,4]
print(my_list_6[-3:-2], "aqui") # [2]

# 15) ??
numsss = [1,2,3]
valsss = numsss[-1:-2] # [3,2]
print(valsss, 'valsss')
print(numsss, 'numsss')

# 16) ??
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*", 'oi')

# 17) 
z = 10
y = 0
x = y < z and z > y or y > z and z < y # True
print(x)

# 18)  ??
my_list_7 = [i for i in range(-1, 2)]
print(my_list_7)