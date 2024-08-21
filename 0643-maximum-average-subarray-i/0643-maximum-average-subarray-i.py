class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        csum = sum(nums[:k])
        msum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            csum += nums[i] - nums[i - k]
            msum = max(msum, csum)
        
        return msum / k




        