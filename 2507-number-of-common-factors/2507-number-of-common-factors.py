class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_factors = 0
        
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                common_factors += 1

        return common_factors
