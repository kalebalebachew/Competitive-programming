# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        lpx = nums[:]
        rpx = nums[:]
        
        for i in range(1, n):
            lpx[i] *= lpx[i-1]

        for i in range(n-2, -1, -1):
            rpx[i] *= rpx[i+1]

        for i in range(n):
            if i == 0:
                res[i] = rpx[i+1]
            elif i == n-1:
                res[i] = lpx[i-1]
            else:
                res[i] = lpx[i-1]*rpx[i+1]  
        return res

             


        