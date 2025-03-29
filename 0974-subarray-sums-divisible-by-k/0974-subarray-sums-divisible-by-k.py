class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_mod_count = {0: 1}  
        prefix_sum = 0
        result = 0 
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k 
            result += prefix_mod_count.get(remainder, 0)
            prefix_mod_count[remainder] = prefix_mod_count.get(remainder, 0) + 1
        
        return result