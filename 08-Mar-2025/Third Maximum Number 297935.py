# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ss = list(set(nums))
        ss.sort()
        for i in range(len(ss)):
            if len(ss) >= 3:
                return ss[-3]
            else:
                return ss[-1]

   