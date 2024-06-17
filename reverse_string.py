# Given an string, return the reverse of it.
# input = hello | output = olleh

# question: 
# 1) can I assume the input will have only letters? yes
# 2) can I assume the input will always have at least one element? yes

# ideia:
# 1) create an empty stack
# 2) traverse the string and for each element
# 3) for each letter in the string, put it on the stack
# 4) initialize an empty string to save the reversed letters
# 5) while the stack is not empty I will pop an item on the stack and save it to the empty string

def reverse_string(string):
    stack = []

    for char in string:
        stack.append(char)
    
    reversed_text = ''

    while stack:
        reversed_text += stack.pop()

    return reversed_text

print(reverse_string('hello'))
print(reverse_string('amandha'))


# considering the memory efficiency when the string is super big, a better approach could be the string builder. 
# this because the concatenate (+=) creates a new space in the memory everytime it is adding a new element on the string. 
#on the other hand, the string builder will insert all the letters at once, without copying the string to add new elements

def reverse_string_builder(string):
    stack = []
    reversed_text_builder = []

    for char in string:
        stack.append(char)
    
    while stack:
        reversed_text_builder.append(stack.pop())

    return ''.join(reversed_text_builder)

print(reverse_string_builder('anotherexampleinabetterperformanceconsideringthememory'))


# follow up: solve the question in-place (not adding extra memory)

def reverse_string_in_place(s):
    # edge cases:
    if len(s) == 0:
        return None
    elif len(s) == 1:
        return s
    
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s

print(reverse_string(['w', 'e', 'l', 'l']))
print(reverse_string(['a', 'm', 'a', 'n', 'd', 'h', 'a']))