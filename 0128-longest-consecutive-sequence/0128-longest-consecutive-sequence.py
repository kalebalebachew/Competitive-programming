class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  
        res = 1
        max_res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                res += 1
            else:
                max_res = max(max_res, res)
                res = 1

        return max(max_res, res)
