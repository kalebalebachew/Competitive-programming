# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        i = 0
        n = len(piles)
        while i < n:
            if i < n // 3:
                i += 1
            else:
                result += piles[i]
                i += 2
        return result


