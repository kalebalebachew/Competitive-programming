# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            isCovered = False

            for i in ranges:
                if i[0] <= x <= i[1]:
                    isCovered = True

            if not isCovered:
                return False
        return True

        