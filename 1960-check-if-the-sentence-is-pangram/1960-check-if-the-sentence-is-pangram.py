class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for s in sentence:
            if s not in d:
                d[s] = 1
            else:
                d[s] +=1
        for key, value in d.items():
            if key in d and len(d) == 26:
                return True
            return False
            
            
        