# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sort_colors(colors):
    left = 0
    right = len(colors) -1
    middle = 0

    while middle <= right:
        if colors[left] > colors[middle]:
            colors[left], colors[middle] = colors[middle], colors[left]
            left += 1
        elif colors[right] < colors[middle]:
            colors[right], colors[middle] = colors[middle], colors[right]
            right -= 1
        middle += 1
    
    return colors

#print(sort_colors([2,0,1]))
print(sort_colors([2,0,2,1,1,0]))
