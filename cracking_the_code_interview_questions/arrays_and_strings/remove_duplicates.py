import unittest
# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. 
# NOTE: One or two additional variables are fine. An extra copy of the array is not. 

# if the interview allow me to change the string (sort it)
# time = O(n log n)
# space = O(1)
def remove_duplicates_no_extra_space(s):
    if len(s) < 2:
        return s
    
    s_sorted = sorted(list(s))
    write_index = 1

    for i in range(1, len(s_sorted)):
        if s_sorted[i] != s_sorted[i - 1]:
            s_sorted[write_index] = s_sorted[i]
            write_index += 1

    return ''.join(s_sorted[:write_index])
print(remove_duplicates_no_extra_space('amandha'))


# if I am not allowed to use additional space AND sort it:
# time = O(n^2)
# space = O(1)
def remove_duplicates_nested_loop(s):
    if len(s) < 2:
        return s
    
    write_index = 1
    s_list = list(s)

    for i in range(1, len(s_list)):
        found_duplicate = False
        for j in range(write_index):
            if s_list[i] == s_list[j]:
                found_duplicate = True
                break

        if not found_duplicate:
            s_list[write_index] = s_list[i]
            write_index += 1

    return ''.join(s_list[:write_index])

print(remove_duplicates_nested_loop('code'))

# write the test cases for this method

class TestRemoveDuplicatesNoExtraSpace(unittest.TestCase):
    def test_one_char_string(self):
        s = 'a'
        result = remove_duplicates_no_extra_space(s)
        assert result == s
    
    def test_char_with_no_duplicates(self):
        s = 'code'
        result = remove_duplicates_no_extra_space(s)
        assert result == 'cdeo'

    def test_char_with_3_duplicates(self):
        s = 'amandha'
        result = remove_duplicates_no_extra_space(s)
        assert result == 'adhmn' # it sorts the array

    def test_char_with_all_duplicates(self):
        s = 'aaaaaaaaaa'
        result = remove_duplicates_no_extra_space(s)
        assert result == 'a'

class TestRemoveDuplicatesNestedLoop(unittest.TestCase):
    def test_one_char_string(self):
        s = 'b'
        result = remove_duplicates_nested_loop(s)
        assert result == s

    def test_char_with_no_duplicates(self):
        s = 'code'
        result = remove_duplicates_nested_loop(s)
        assert result == s

    def test_char_with_2_duplicates(self):
        s = 'well'
        result = remove_duplicates_nested_loop(s)
        assert result == 'wel'

    def test_char_with_all_duplicates(self):
        s = 'aaaaaaaaaa'
        result = remove_duplicates_no_extra_space(s)
        assert result == 'a'

    


if __name__ == '__main__':
    unittest.main()