# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = { 'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        total = 0
        pvalue = 0

        for c in reversed(s):
            cvalue = dic[c]

            if cvalue < pvalue:
                total -= cvalue
            else:
                total += cvalue
            pvalue = cvalue
        return total


        
        