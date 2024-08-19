class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            sth = target - n
            if sth in dic:
                return [dic[sth], i]
            dic[n] = i
        return []
        

 


       


         
            




            
            
            
                
                    
                
                
                
                    




            

            
            
            
       


