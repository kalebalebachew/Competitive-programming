class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        
        nums.sort()
        l = 1
        c = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                c += 1
            else:
                c = 1 
            l = max(l, c)
        
        return l
