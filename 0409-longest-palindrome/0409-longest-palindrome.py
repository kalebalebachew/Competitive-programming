class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        longest = 0
        odd = False

        for count in c.values():
            longest += count // 2 * 2
            if count % 2 == 1:
                odd = True

        if odd:
            longest += 1

        return longest




        

        

        