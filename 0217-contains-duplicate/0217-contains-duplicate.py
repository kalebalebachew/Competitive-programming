class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        k = set()
        for num in nums:
            if num in k:
                return True
            else:
                k.add(num)
        
        return False
            
        