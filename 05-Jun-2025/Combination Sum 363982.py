# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(remain: int, curr_comb: list[int], start: int):
            if remain == 0:
                res.append(curr_comb[:])
                return
            if remain < 0:
                return
                
            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])
                backtrack(remain - candidates[i], curr_comb, i)
                curr_comb.pop()
        
        backtrack(target, [], 0)
        return res
        
        