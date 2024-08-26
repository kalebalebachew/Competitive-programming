class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        so = sorted(c.items(), key=lambda x: -x[1])

        res = [item[0] for item in so[:k]]

        return res
       


     
            

        
     

