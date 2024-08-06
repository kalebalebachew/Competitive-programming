class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        numsone = sorted(nums1)
        numstwo = sorted(nums2)
        ans = []
        l = 0
        r = 0
        while l < len(numsone) and r < len(numstwo):
            if numsone[l] < numstwo[r]:
                l += 1
            elif numsone[l] > numstwo[r]:
                r += 1
            else:
                ans.append(numsone[l])
                l += 1
                r += 1

        return ans


        