def singleNumber(nums):
    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        hash_map[num] = 1

    for key, value in hash_map.items():
        if value == 1:
            return key
        
nums = [3,2,2,1]
print(singleNumber(nums))