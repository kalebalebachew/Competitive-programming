# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in reversed(range(n)):
            mx = arr.index(max(arr[:i+1]))
            
            if mx != i:
                if mx != 0:
                    arr[:mx+1] = arr[:mx+1][::-1]
                    res.append(mx + 1)  
                arr[:i+1] = arr[:i+1][::-1]
                res.append(i + 1)
        
        return res
