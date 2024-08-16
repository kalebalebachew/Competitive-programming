class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence.lower()
        k = set('abcdefghijklmnopqrstuvwxyz')
    
        if k.issubset(s):
            return True
        else:
            return False


            
            
        