class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        prevmap = {}
        count = 0 

        for num in nums:
            if num not in prevmap:
                prevmap[num] = 1
            else:
                prevmap[num] += 1

        for key, value in prevmap.items():
            target = key - k
            if target in prevmap:
                count += prevmap[target] * prevmap[target + k]
                

        return count