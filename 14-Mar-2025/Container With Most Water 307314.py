# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = max(area, h*w)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
        

        