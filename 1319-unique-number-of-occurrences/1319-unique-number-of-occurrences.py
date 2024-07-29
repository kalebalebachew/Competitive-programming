class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for a in arr:
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
        
        occurrences = set(dic.values())
        return len(occurrences) == len(dic)