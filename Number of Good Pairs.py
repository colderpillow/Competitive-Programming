class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i] == nums[j]:
                    good += 1
        return(good)
