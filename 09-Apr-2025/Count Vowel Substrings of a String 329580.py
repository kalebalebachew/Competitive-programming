# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v = set("aeiou")  
        c = 0 
        for i in range(len(word)):
            if word[i] not in v:
                continue    
            seen = set()     
            for j in range(i, len(word)):
                if word[j] not in v:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    c += 1
        return c
