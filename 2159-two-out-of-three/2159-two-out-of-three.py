class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    
 
        common12 = set1 & set2
        common13 = set1 & set3
        common23 = set2 & set3
    
   
        result = common12 | common13 | common23
    
   
        return list(result)
