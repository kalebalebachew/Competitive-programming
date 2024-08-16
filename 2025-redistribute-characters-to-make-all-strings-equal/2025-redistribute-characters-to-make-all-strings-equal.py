class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        k = defaultdict(int)
        
        for word in words:
            for c in word:
                k[c] +=1
                
        
        for count in k.values():
            if count % len(words) != 0:
                return False
        
        return True

        