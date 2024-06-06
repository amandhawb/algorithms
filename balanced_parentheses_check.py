# given an string containing parentheses in pairs (example: "()", "[]", and "{}") 
# ensure that each opening parentheses has a corresponding closing parentheses of the same type in the correct order.

# example: 
# input = "{[()]}" | output = true
# input = "{([)]}" | output = false

# questions:
# 1) can I assume there is only these special caracters - (), [], and {}, no letters or numbers? Yes

# idea:
# 1) initialize an empty stack
# 2) create a hash map to store open and closing elements, just to be a reference when checking
# 3) loop through the string:
#    - if the current character is open - ( or [ or { - I will append it on the stack
#    - if the current character is close - ) or ] or } - I will:
#       - check if the stack is empty, if it is, I can return false because it means that I have an extra closing element
#       - check if my last element on the stack is the opposite (the opening) of my current closing element:
#           - if the element is not the oposite, it means the string is not balanced, so return false
#           - if it is the oposite, I don't do nothing, I just go to the next element
# 4) in the end of the loop, if the stack is empty, I return true, if not (which means there is an extra opening), I return false


def balanced_check(string):
    stack = []
    hash_map = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for item in string:
        if item in hash_map:
            stack.append(item)
        elif item in hash_map.values():
            if len(stack) == 0:
                return False
            last_element = stack.pop()
            if hash_map[last_element] != item:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False

print(balanced_check("{[()]}"))
print(balanced_check("{[()}"))
print(balanced_check("{[(])}"))
print(balanced_check("{[()]}("))
print(balanced_check("{[()]})"))
print(balanced_check("){[()]}"))