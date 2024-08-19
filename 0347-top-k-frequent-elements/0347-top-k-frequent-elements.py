class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        
        most_common = freqDict.most_common(k)
        
        res = [item[0] for item in most_common]
        
        return res
