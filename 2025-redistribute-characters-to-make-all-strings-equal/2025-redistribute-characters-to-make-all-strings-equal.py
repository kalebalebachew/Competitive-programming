class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        k = {}
        
        for word in words:
            for c in word:
                if c in k:
                    k[c] +=1
                else:
                    k[c] = 1
                
        
        for count in k.values():
            if count % len(words) != 0:
                return False
        
        return True

        