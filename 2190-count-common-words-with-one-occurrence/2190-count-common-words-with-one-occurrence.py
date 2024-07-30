class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        dic = {}

        for word in words1:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        for word in words2:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        for word,counts in dic.items():
            if counts == 2 and word in words1 and word in words2:
                count += 1
            
        return count

           

        
        