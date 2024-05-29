class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> int:
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
    

    print(topKFrequent(self = None, nums = [1,2,2,1,4,5], k = 2))