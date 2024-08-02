class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        freq = max(dic.values())
        for num in dic.values():
            if freq == num:
                count += 1
        return count*freq
                
        
            
                

        