class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        for char in "qwertyuiop":
            dic[char] = 1
        for char in "asdfghjkl":
            dic[char] = 2
        for char in "zxcvbnm":
            dic[char] = 3
        
        result = []
        
        for word in words:
            first = dic[word[0].lower()]
            
            if all(dic[char.lower()] == first for char in word):
                result.append(word)
        
        return result
