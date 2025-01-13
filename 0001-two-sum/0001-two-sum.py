class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            
            if num not in hashmap:
                hashmap[num] = i


       


         
            




            
            
            
                
                    
                
                
                
                    




            

            
            
            
       


