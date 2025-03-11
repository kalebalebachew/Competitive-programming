class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for s in range(len(nums)):
            res = [nums[s]]
            curr = nums[s]
            for i in range(s+1, len(nums)):
                if nums[i] == curr**2:
                    res.append(nums[i])
                    curr = nums[i]
            if len(res) > mx:
                mx = len(res)
        return mx if mx >= 2 else -1


     

        