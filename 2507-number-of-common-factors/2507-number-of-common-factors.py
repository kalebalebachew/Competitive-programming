import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_ab = math.gcd(a, b)
        count = 0
        sqrt_gcd = int(math.sqrt(gcd_ab))
        
        for i in range(1, sqrt_gcd + 1):
            if gcd_ab % i == 0:
                count += 1  
                if i != gcd_ab // i:
                    count += 1  
        
        return count
