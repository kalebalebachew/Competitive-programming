class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        csum = 0

        for i in range(k):
            csum += nums[i]

            mavg = csum / k
        for i in range(k, n):
            csum += nums[i]
            csum -= nums[i-k]

            a = csum / k
            mavg = max(mavg, a)

        return mavg






        