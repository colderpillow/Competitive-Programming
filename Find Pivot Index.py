class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_right = [nums[0]]
        len_nums = len(nums)
        right_left = [nums[-1]]
        ans = -1
        for i in range(1, len_nums):
            left_right.append(nums[i]+left_right[i-1])

        for i in range(2, len_nums+1):
            right_left.insert(0, nums[-i]+right_left[-i+1])

        for i in range(len_nums):
            if left_right[i] == right_left[i]:
                ans = i
                break

        return ans
