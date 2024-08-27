class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        mx = 0
        l = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            mx = max(mx, r- l + 1 ) 
        return mx


        