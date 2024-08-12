class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_map = {}
    
        for num in nums:
            num_map[num] = True
        
        for i in range(len(nums) + 1):
            if i not in num_map:
                return i
        