class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        k = {}

        for i in s:
            if i in k:
                k[i]+=1
            else:
                k[i] = 1
        for j in t:
            if j in k:
                k[j] -= 1
            else:
                return False
        for g in k.values():
            if g != 0:
                return False
            else:
                return True
        