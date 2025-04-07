class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = {"a": 0, "b": 0, "c": 0}
        res = 0
        l = 0
        for r in range(len(s)):
            c[s[r]] += 1
            while c['a'] > 0 and c['b'] > 0 and c['c'] > 0:
                res += len(s) - r
                c[s[l]] -= 1
                l += 1

        return res
