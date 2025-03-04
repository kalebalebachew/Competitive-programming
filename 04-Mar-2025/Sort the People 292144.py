# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            mi = i 
            for j in range(i + 1, n):
                if heights[j] > heights[mi]: 
                    mi = j
            if mi != i:
                heights[i] , heights[mi] = heights[mi] , heights[i]
                names[i] , names[mi] = names[mi], names[i]
            
        return names 
