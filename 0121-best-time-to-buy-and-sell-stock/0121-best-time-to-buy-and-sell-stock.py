class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ans = 0
        for price in prices:
            if price < mi:
                mi = price
            ans = max(ans, price - mi)
        return ans
    



       


        