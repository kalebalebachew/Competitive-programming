from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ml = float('inf')  
        l = 0              
        csum = 0          
        
        for r in range(len(nums)):
            csum += nums[r]
            
            while csum >= target:
                ml = min(ml, r - l + 1) 
                csum -= nums[l]
                l += 1
        
        return ml if ml != float('inf') else 0
