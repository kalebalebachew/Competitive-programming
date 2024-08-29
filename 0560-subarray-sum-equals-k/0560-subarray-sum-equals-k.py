class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        csum = 0
        ps = defaultdict(int)
        ps[0] = 1 
        
        for num in nums:
            csum += num
            
            if (csum - k) in ps:
                count += ps[csum - k]
            
            ps[csum] += 1
        
        return count