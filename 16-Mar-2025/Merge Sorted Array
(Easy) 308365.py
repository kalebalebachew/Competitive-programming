# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        l = 0
        r = 0
        
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        while l < m:
            res.append(nums1[l])
            l += 1
        
        while r < n:
            res.append(nums2[r])
            r += 1
        for i in range(m + n):
            nums1[i] = res[i]
