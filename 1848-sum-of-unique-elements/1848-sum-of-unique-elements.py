class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        count = 0
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for key, value in d.items():
            if value == 1:
                
                count += key
                
            

        return count
    

        


        