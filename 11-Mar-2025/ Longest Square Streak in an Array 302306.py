# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ss = set(nums)
        mx = 0
        for num in nums:
            res = [num]
            curr = num
            while curr * curr in ss:
                curr = curr * curr
                res.append(curr)
            mx = max(mx , len(res))
        return mx if mx >= 2 else -1

  


     

        