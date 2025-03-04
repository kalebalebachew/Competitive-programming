# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            midx = i
            for j in range(i+1, len(nums)):
                if nums[midx] > nums[j]:
                    midx = j
            nums[i], nums[midx] = nums[midx], nums[i]
        for k in range(len(nums)):
            if nums[k] == target:
                res.append(k)
        return res

        