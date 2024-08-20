class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        for i,j in hm.items():
            if j > n //2:
                return i
        return -1

            
       
       
