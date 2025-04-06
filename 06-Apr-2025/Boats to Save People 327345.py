# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = people
        p.sort(reverse=True)
        b = 0
        i = 0
        j = len(p) - 1
        while i <= j:
            if i == j:
                b += 1
                break
            if i < j and p[i] + p[j] <= limit:
                i += 1
                j -= 1
            else:
                i += 1
            b += 1
        return b