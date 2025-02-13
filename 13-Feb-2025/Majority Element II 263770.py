# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        res = []
        for k,v in c.items():
            if v > n // 3:
                res.append(k)
        return res


        