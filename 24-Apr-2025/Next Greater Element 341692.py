# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nx = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                nx[stack.pop()] = num
            stack.append(num)
        while stack:
                nx[stack.pop()] = -1
        res = [nx[num] for num in nums1]
        return res
        