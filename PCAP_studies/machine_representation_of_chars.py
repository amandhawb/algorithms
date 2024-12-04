# ASCII Practice:
# Print the ASCII code for a given character using ord().
# Convert an ASCII code back to a character using chr().
print(ord('a'))
print(ord('A'))
print(chr(97))
print(chr(65))
print(chr(126))

# UTF-8 Practice:
# Encode a string into UTF-8 and decode it back using .encode() and .decode().
res = 'amandha'.encode()
print(res)
print(res.decode())