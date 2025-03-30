
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        seen = {0: -1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r < 0:
                r += k
            if r in seen:
                if i - seen[r] > 1:
                    return True
            else:
                seen[r] = i

        return False