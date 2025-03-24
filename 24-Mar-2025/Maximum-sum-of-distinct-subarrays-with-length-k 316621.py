# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        msum = 0
        wsum = 0
        l = 0

        for r in range(len(nums)):
            wsum += nums[r]
            dic[nums[r]] = dic.get(nums[r], 0) + 1

            if r - l + 1 > k:
                wsum -= nums[l]
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1

            if r - l + 1 == k and len(dic) == k:
                msum = max(msum, wsum)
                
        return msum
