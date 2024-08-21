class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for k in s:
            if k in hm:
                hm[k] += 1
            else:
                hm[k] = 1
        
        for i, k in enumerate(s):
            if hm[k] == 1:
                return i
        
        return -1
