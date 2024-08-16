class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if set('abcdefghijklmnopqrstuvwxyz').issubset(sentence.lower()):
            return True
        else:
            return False




            
            
        