class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            if key in count:
                good_pairs += count[key]
                count[key] += 1
            else:
                count[key] = 1

        total_pairs = len(nums) * (len(nums) - 1) // 2
        bad_pairs = total_pairs - good_pairs
        
        return bad_pairs


       


    


     


        