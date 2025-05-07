# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2  
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m - 1
        return l

        