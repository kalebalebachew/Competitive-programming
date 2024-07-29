class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        res = 0

        for i, num in enumerate(nums):
            d[num] = 1

        for i in range(len(nums) + 1):
            if i not in d:
                res = i

        return res
            
        