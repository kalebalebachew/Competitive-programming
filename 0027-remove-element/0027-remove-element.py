class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_map = Counter(nums)      
        new_index = 0
        for num in nums:
            if num != val:
                nums[new_index] = num
                new_index += 1
    
  
        new_length = len(nums) - count_map.get(val, 0)
    
        return new_length
    

        