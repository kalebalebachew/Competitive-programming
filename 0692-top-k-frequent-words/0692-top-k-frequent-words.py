class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
 
        c = Counter(words)

        so = sorted(c.items(), key=lambda x: (-x[1], x[0]))

        res = [item[0] for item in so[:k]]

        return res

        