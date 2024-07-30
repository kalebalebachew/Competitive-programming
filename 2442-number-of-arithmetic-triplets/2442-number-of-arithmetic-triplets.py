class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplet = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == diff:
                    # Check for third element
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] == diff:
                            triplet += 1
        return triplet
            
