class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        result = 0

        # Count the occurrences of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Calculate the number of good pairs for each number
        for num in count:
            n = count[num]
            result += n * (n - 1) // 2

        return result

# Example usage:
solution = Solution()

nums1 = [1, 2, 3, 1, 1, 3]
print(solution.numIdenticalPairs(nums1))  # Output: 4

nums2 = [1, 1, 1, 1]
print(solution.numIdenticalPairs(nums2))  # Output: 6

nums3 = [1, 2, 3]
print(solution.numIdenticalPairs(nums3))  # Output: 0
