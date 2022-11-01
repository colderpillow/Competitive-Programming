class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = 0
        lesser = []
        for i in nums:
            num = 0
            for j in nums:
                if j < i:
                    num += 1
            lesser.append(num)
            
        return(lesser)
