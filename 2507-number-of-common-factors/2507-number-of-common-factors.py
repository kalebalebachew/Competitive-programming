import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        gcd_ab = math.gcd(a, b)
        for i in range(1, int(math.sqrt(gcd_ab)) + 1):
            if gcd_ab % i == 0:
                count += 1
                if i != gcd_ab // i:
                    count += 1
        
        return count
