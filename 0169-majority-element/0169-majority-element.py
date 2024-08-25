class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for i,k in c.items():
            if k > n // 2:
                return i
        return -1


      
            
       
       
