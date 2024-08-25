class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        pal = 0
        while y != 0:
            r = y % 10
            pal = pal * 10 + r
            y = y // 10

        return x == pal
       
        