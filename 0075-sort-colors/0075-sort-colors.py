class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        swapped = True
        while swapped:
            swapped = False
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
