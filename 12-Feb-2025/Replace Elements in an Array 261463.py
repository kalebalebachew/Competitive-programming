# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        ans = [0] * len(nums)

        for i in range(len(nums)):
            d[nums[i]] = i

        for i, j in operations:
            if i in d:
                d[j] = d.pop(i)

        for i, j in d.items():
            ans[j] = i

        return ans
