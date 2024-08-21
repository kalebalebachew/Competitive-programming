class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()  
        res = 0 
        
        for num in nums:
            if num not in seen:
                seen.add(num)  
                nums[res] = num  
                res += 1  
        
        return res  


                
    




    

            


        