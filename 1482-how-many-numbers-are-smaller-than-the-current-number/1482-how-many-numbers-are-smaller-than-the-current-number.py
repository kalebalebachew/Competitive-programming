from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Create a list to store the counts of each number
        counts = [0] * 101  # Since the given constraint is 0 <= nums[i] <= 100

        # Count the occurrences of each number in the input array
        for num in nums:
            counts[num] += 1

        # Update the counts to represent the number of elements smaller than or equal to each number
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        # Use counts to get the result for each element in the original array
        result = [counts[num - 1] if num > 0 else 0 for num in nums]

        return result
