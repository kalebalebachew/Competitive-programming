# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        c = 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                c += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1
        return c

        