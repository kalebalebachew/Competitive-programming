# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total < x:
            return -1
        if total == x:
            return len(nums)
            
        t = total - x
        n = len(nums)
        
        csum = 0
        mx = -1
        l = 0
        
        for r in range(n):
            csum += nums[r]
            
            while csum > t and l <= r:
                csum -= nums[l]
                l += 1
            
            if csum == t:
                mx = max(mx, r - l + 1)
        
        return -1 if mx == -1 else n - mx

