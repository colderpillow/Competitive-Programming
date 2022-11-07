class Solution:
    def productExceptSelf(self, nums):
        pre_prod = [nums[0]]
        ford_prod = [nums[-1]]

        nums_len = len(nums)

        for i in range(1, nums_len):
            pre_prod.append(pre_prod[i-1]*nums[i])
            ford_prod.insert(0, ford_prod[-i]*nums[-i-1])

        ans = [
            ford_prod[1]
        ]

        for i in range(1, nums_len):
            if i == (nums_len-1):
                ans.append(pre_prod[i-1])
            else:
                ans.append(pre_prod[i-1]*ford_prod[i+1])
        return ans
