class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        s = []
        for i in range(len(nums)):
            while s and nums[s[-1]] < nums[i]:
                res[s[-1]] = nums[i]
                s.pop()
            s.append(i)
        for i in range(len(nums)):
            while s and nums[s[-1]] < nums[i]:
                res[s[-1]] = nums[i]
                s.pop()
        return res
        