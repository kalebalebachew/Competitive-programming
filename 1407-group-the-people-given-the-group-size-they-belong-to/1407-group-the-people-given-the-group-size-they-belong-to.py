class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        result = []
        
        for id, size in enumerate(groupSizes):
            dic[size].append(id)
            
            if len(dic[size]) == size:
                result.append(dic[size])
                dic[size] = []  
        
        return result

        