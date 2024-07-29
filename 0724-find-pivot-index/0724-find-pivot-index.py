class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        count = 0
        sum_array = sum(nums)
        for i in range(len(nums)):
          count += nums[i]
          if sum_array == count:
              return i
          sum_array -= nums[i]
        return -1

        


        


        

        