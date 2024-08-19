class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum in dic:
                return True
            dic[sum] = sum
        return False
        
            
            
         



        

        



        