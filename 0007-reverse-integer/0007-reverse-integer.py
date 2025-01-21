class Solution:
    def reverse(self, x: int) -> int:
        min, max = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1

        rev = int(str(abs(x))[::-1]) * sign

        if rev < min or rev > max:
            return 0
        
        return rev



        