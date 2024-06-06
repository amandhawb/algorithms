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