class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        for s in s1.split(" "):
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1
        for s in s2.split(" "):
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1 
        return [x for x in dic.keys() if dic[x]==1]


      

    
          
      
        

        
        