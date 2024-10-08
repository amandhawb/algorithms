def decode_string(s):
    stack = []
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substring = ""
            while stack[-1] != "[":
                substring = stack.pop() + substring
            stack.pop() # the "[" element needs to be popped from the stack
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substring)
    return "".join(stack)


# TEST

print(decode_string("3[a]2[bc]")) # "aaabcbc"
print(decode_string("3[a2[c]]")) # "accaccacc"
print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"
