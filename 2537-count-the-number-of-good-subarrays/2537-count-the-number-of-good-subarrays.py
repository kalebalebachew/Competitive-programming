class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0  
        pairs = 0  
        freq = defaultdict(int)  
        left = 0  
        
        for right in range(len(nums)):
            curr = nums[right]
            pairs += freq[curr]  
            freq[curr] += 1  
            
            while pairs >= k:
                count += len(nums) - right 
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]] 
                left += 1
        
        return count
        