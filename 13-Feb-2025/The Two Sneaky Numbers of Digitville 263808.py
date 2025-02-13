# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ss = set()
        ans = []
        for num in nums:
            if num in ss:
                ans.append(num)
            else:
                ss.add(num)
        return ans

        