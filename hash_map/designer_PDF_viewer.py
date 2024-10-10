# FIRST VERSION (by myself)
# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. 
# There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mmˆ2 assuming all letters are 1mm wide.
# example:
# h = 1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5] word - torn
# The heights are t = 2, o = 1, = 1 and n = 1. The tallest letter is 2 high and there are 4 letters. The highlighted area will be 2 * 4 = 8mm? so
# the answer is 8.

# time = O(n) --> because of the sorting method
# space = O(n) --> where n is the word size
def designer_pdf_viewer(h, word):
    hash_map = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25
    }

    letters_size = []

    for letter in word:
        letter_position = hash_map[letter]
        letter_size = h[letter_position]
        letters_size.append(letter_size)
    
    return max(letters_size) * len(letters_size)


# TEST
print(designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7,
], "zaba")) # 28
print(designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
], "abc")) # 9
