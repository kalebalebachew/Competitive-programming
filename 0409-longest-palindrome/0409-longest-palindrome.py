class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        longest = 0
        odd = False

        for count in c.values():
            if count % 2 == 0:
                longest += count 
            else:
                longest += count - 1 
                odd = True  

        if odd:  
            longest += 1

        return longest




        

        

        