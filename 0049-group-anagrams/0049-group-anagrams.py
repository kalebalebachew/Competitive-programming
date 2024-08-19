class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict ={}
        for s in strs:
            sth = "".join(sorted(s))
            if sth not in dict:
                dict[sth] = [s]
            else:
                dict[sth].append(s)
        return dict.values()



     

        