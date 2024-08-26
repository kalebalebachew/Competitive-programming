class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd = 0
        c = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd += 1
                c = 0
            while odd == k:
                c += 1
                if nums[left] % 2 != 0:
                    odd -=1
                left += 1

            res += c

        return res
       



            
        
            



        