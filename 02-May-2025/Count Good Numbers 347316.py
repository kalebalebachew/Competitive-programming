# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        md = 10**9 + 7 
        ev = pow(5, (n + 1) // 2, md)
        od = pow(4, n // 2, md)
        return (ev * od) % md