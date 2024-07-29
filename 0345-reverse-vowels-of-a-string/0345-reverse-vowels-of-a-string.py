class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = set('aeiouAEIOU')
        sl = list(s)
        
        while l < r:
            if sl[l] in vowels and sl[r] in vowels:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
            elif sl[l] in vowels:
                r -= 1
            elif sl[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1

        return ''.join(sl)

        

        