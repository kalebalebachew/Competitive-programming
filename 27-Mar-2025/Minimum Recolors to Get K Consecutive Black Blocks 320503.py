# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self,blocks: str, k: int) -> int:
        wc = blocks[:k].count('W')
        mn = wc
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                wc -= 1
            if blocks[i] == 'W':
                wc += 1
            mn = min(mn, wc)
        
        return mn
        