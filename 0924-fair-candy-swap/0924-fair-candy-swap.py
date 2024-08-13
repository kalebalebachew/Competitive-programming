class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        bobDict = {candy: True for candy in bobSizes}
        
        for candyA in aliceSizes:
            targetCandyB = candyA + (sumB - sumA) // 2
            if targetCandyB in bobDict:
                return [candyA, targetCandyB]
        