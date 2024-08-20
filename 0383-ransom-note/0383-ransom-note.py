class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)

        for m in magazine:
            if m in dic:
                dic[m] += 1
            else:
                dic[m] = 1

        for r in ransomNote:
            if dic[r] > 0:
                dic[r] -= 1
            else:
                return False
        
        return True
        
        


        

        