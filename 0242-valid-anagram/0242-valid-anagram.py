class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for k in s:
            dic[k] += 1
        for k in t:
            dic[k] -= 1

        for v in dic.values():
            if v != 0:
                return False
        return True

        
        