class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            if num-1 not in nums:
                cn = num
                length = 1
                while cn + 1 in nums:
                    cn += 1
                    length += 1
                longest = max(longest, length)
        return longest

       


      
            



      




        
