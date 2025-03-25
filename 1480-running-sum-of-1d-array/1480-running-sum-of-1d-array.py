class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        t = 0
        for num in nums:
            t += num
            res.append(t)
        return res

        