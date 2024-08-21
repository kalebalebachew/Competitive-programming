class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        n = len(nums)
        result = []

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        for num, count in hm.items():
            if count > n // 3:
                result.append(num)

        return result

