# You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.
# You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:
# guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
# If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
# If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
# Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_order(arrival_pattern):
    result = []
    stack = []
    digit = 1

    for i in range(len(arrival_pattern) +1):
        stack.append(str(digit))
        digit += 1

        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())

    return ''.join(result)

# TEST
print(arrange_guest_order("IDID"))  # Expected Output: "13254"
print(arrange_guest_order("III"))  # Expected Output: "1234"
print(arrange_guest_order("DDD"))  # Expected Output: "4321"
print(arrange_guest_order("I"))  # Expected Output: "12"
print(arrange_guest_order("D"))  # Expected Output: "21"
print(arrange_guest_order("DDIDDIID"))  # Expected Output: "321654789"
