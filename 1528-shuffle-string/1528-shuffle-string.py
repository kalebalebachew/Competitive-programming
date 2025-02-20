class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuff = [''] * len(s)
        for i in range(len(s)):
            shuff[indices[i]] = s[i]
        return ''.join(shuff)


        