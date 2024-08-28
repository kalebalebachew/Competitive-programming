class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        so = sorted(c.items(), key=lambda x: -x[1])

        res = [i[0] for i in so[:k]]

        return res
       


     
            

        
     

