class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum = set()

        for i in range(len(nums)- 1):
            n = nums[i] + nums[i+1]
            if n in sum:
                return True
            else:
                sum.add(n)
        return False

        

        



        