class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m 
            else:
                l = m + 1  
        
        return l + 1 if nums[l] < target else l



        