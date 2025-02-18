class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
            else:
                continue
                
        zero = 0
        for c in range(len(nums)):
            if nums[c] != 0:
                nums[zero], nums[c] = nums[c], nums[zero]
                zero += 1
            
        return nums
        
            



        