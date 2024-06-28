def validate_stack(pushed, popped):
    stack = []
    i = 0

    for num in pushed:
        stack.append(num)
        while i < len(popped) and stack and popped[i] == stack[-1]:
            stack.pop()
            i += 1
    
    if len(stack) == 0:
        return True
    else:
        return False


print(validate_stack([1,2,3,4,5], [4,5,3,2,1]))
print(validate_stack([1,2,3,4,5], [4,3,5,1,2]))
print(validate_stack([1,0], [1,0]))