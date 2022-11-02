class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        out = []
        for i in range(len(arr)):
            if arr[i] == target:
                out.append(i)
        return(out)
        
