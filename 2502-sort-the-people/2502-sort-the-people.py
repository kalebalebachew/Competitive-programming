class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic= {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        sortedd = dict(sorted(dic.items()))
        return reversed(sortedd.values())




        