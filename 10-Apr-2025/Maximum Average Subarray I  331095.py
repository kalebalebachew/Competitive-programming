# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum = 0
        msum = float('inf')
        for i in range(k):
            wsum += nums[i]
        msum = wsum
        l = 0
        for r in range(k, len(nums)):
            wsum += nums[r]
            wsum -= nums[l]
            msum = max(msum, wsum)
            l += 1
        return msum / k


        


        