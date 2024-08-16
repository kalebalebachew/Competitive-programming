class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        k = min(strs, key=len)
        
        for i, char in enumerate(k):
            for other in strs:
                if other[i] != char:
                    return k[:i]
        return k


        