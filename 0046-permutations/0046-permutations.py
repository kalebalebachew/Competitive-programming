class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res = [perm[:i] + [num] + perm[i:] for perm in res for i in range(len(perm) + 1)]
        return res
        