class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        prevmap = {}
        countt = 0

       
        for num in nums:
            if num in prevmap:
                prevmap[num] += 1
            else:
                prevmap[num] = 1

       
        for count in prevmap.values():
            countt += count * (count - 1) // 2

        return countt

        