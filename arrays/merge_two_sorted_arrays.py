# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def merge_two_stored_arrays_in_place(nums1, m, nums2, n):
    index1 = m - 1
    index2 = n - 1
    insertIndex = (m + n) - 1

    while index2 >= 0:
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            nums1[insertIndex] = nums1[index1]
            index1 -= 1
        else:
            nums1[insertIndex] = nums2[index2]
            index2 -= 1
        insertIndex -= 1
    

# TODO: solve in O(n) space
# def merge_two_sorted_arrays
