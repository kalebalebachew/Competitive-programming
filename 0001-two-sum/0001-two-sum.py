class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goddamn_hashmap = {}

        for i, v in enumerate(nums):
            c = target - v
            if c in goddamn_hashmap:
                return [goddamn_hashmap[c], i]
            else:
                goddamn_hashmap[v] = i
        return []

       
        
                

        
                

        
       



        
       

 


       


         
            




            
            
            
                
                    
                
                
                
                    




            

            
            
            
       


