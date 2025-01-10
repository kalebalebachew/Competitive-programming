class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        dic1 = {}
        dic2 = {}
        
        for s1,t1 in zip(s,t):
            if s1 in dic1 and dic1[s1] != t1:
                return False
            else:
                dic1[s1] = t1
        
        for s1,t1 in zip(s,t):
            if t1 in dic2 and dic2[t1] !=  s1:
                return False
            else:
                dic2[t1] = s1
        
        return True
            