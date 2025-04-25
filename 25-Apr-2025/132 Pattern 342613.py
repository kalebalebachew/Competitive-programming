# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s2 = float('-inf')
        for num in reversed(nums):
            if num < s2:
                return True
            while stack and stack[-1] < num:
                s2 = stack.pop()
            stack.append(num)
        return False