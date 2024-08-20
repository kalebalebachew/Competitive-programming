class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hm = {}

        for r in t:
            if r in hm:
                hm[r] += 1
            else:
                hm[r] = 1
        
        for r in s:
            if r in hm:
                hm[r] -= 1
        
        for k, v in hm.items():
            if v > 0:
                return k


        
        
        