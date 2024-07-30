class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for char in s:
            if char in dic:
                return char
            else:
                dic[char] = 1
        
            


        