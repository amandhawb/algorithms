set1 = input().split()
set2 = input().split()

common_chars = []

for char in set1:
    if char in set2:
        common_chars.append(char)
        
common_chars.sort()

if common_chars:
    print(' '.join(common_chars))
else:
    print('NULL')
