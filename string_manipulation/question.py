input_string = "Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;"
import re

distances = re.findall(r'\d+', input_string)
distances = [int(num) for num in distances]

print(distances, 'before')
distances.sort()
print(distances, 'after')

current_distance = 0
result = []

for distance in distances:
    difference = distance - current_distance
    result.append(difference)
    current_distance = distance
    
print(','.join(str(x) for x in result))

# result_in_string = str(result)

# print(result_in_string)

# RESULTADO:

for line in sys.stdin:
    input_string = line

distances = re.findall(r'\d+', input_string)
distances = [int(num) for num in distances]
distances.sort()

current_distance = 0
result = []

for distance in distances:
    difference = distance - current_distance
    result.append(difference)
    current_distance = distance
    
print(','.join(str(x) for x in result))





# MELHORADO:

import sys
input_string = ''
for line in sys.stdin:
    input_string = line.strip()

distances = []
for item in input_string.split(';'):
    if ',' in item:
        number = item.split(',')[1].strip()
        distances.append(int(number))
        
distances.sort()


current_distance = 0
result = []

for distance in distances:
    difference = distance - current_distance
    result.append(difference)
    current_distance = distance
    
print(','.join(str(x) for x in result))