# Given an string with a couple of letters and a substring, find how many times the substring is seen in the string
# Example:
# string = "dadaddadaadada"
# substring = "dad"
# answer = 4

# time = O(n)
# space = O(1)
def counter(string, sub):
    result = 0
    sub_size = len(sub)
    for i in range(len(string)):
        if string[i:i+sub_size] == sub:
            result += 1
    return result

print(counter("dadaddadaadada", "dad")) # 4
print(counter("momommomomommo", "mom")) # 5