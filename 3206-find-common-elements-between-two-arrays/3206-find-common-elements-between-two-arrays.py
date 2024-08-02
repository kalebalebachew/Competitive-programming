class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        for n in nums1:
            if n in nums2:
                count1 += 1
        for n in nums2:
            if n in nums1:
                count2 += 1
        return count1, count2
        
    

                

        