# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dc={
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, k):
            if len(k)==len(digits):
                res.append(k)
                return
            for c in dc[digits[i]]:
                dfs(i+1, k+c)
        if  digits:
            dfs(0,"")
        return res