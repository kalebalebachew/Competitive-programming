from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        k = 0

        for num, count in dic.items():
            if count >= 2:
                k += count // 2

        return [k, len(nums) - k * 2]