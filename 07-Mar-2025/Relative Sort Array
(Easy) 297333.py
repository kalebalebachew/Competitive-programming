# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mx = max(arr1) 
        count = [0] * (mx + 1)  
        for num in arr1:
            count[num] += 1
        
        res = []
        
        for num in arr2:
            res.extend([num] * count[num])
            count[num] = 0  
        
        for num in range(mx + 1):
            if count[num] > 0:
                res.extend([num] * count[num]) 
        
        return res




        