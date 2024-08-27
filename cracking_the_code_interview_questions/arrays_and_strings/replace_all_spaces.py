# write a method to replace all spaces in a string with `%20`.

def replace_spaces(s):
    s_list = list(s)
    for char in range(len(s_list)):
        if s_list[char] == ' ':
            s_list[char] = '%20'
    
    return ''.join(s_list)

print(replace_spaces('eu amo voce'))
print(replace_spaces('amandha'))
print(replace_spaces('amandha wingert barok de souza'))
print(replace_spaces('      '))