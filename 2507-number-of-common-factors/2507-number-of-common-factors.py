import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_ab = math.gcd(a, b)
        count = 0
        for i in range(1, gcd_ab + 1):
            if gcd_ab % i == 0:
                count += 1
            
        return count


