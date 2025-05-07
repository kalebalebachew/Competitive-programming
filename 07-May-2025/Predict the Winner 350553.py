# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            return max(
                nums[left] - dp(left + 1, right),
                nums[right] - dp(left, right - 1)
            )
        n = len(nums)
        return dp(0, n - 1) >= 0