def topKFrequent(nums, k):
    nums.sort()
    print(nums)

    seen = 0

    for i in range(len(nums)):
        print(i)
        if nums[i] == nums[i-1]:
            print("entered")
            seen += 1
        else:
            if seen == k:
                return nums[i -1]
            else:
                seen = 0
    print(seen, "seen")
    return None
    

print(topKFrequent([1,2,2,1,4,5], 2))