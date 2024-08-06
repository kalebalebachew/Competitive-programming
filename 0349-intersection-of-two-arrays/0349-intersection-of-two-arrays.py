class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1m = {}
        # num2m = {}
        
        # for num in nums1:
        #     if num in num1m:
        #         num1m[num] += 1
        #     else:
        #         num1m[num] = 1
        
        # for num in nums2:
        #     if num in num2m:
        #         num2m[num] += 1
        #     else:
        #         num2m[num] = 1
        
        # res = []
        # for num in num1m.keys():
        #     if num in num2m:
        #         res.append(num)
        
        # return res
        num1 = set(nums1)
        num2 = set(nums2)
        inter = []
        for ele  in num1:
            if ele in num2:
                inter.append(ele)
        return inter


        