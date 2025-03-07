class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        c = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                res += len(nums) - i
        return res 

        