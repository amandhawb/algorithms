# Write a code to reverse a string
def reverse_string(text):
    return text[::-1] # slice notation [start:stop:step] allows me to specify a step value of -1, which reverses the string.

print(reverse_string('hello'))
print(reverse_string('amandha'))