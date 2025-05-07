# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self,tickets: list[int], k: int) -> int:
        t = 0
        tg = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                t += min(tickets[i], tg)
            else:
                t += min(tickets[i], tg - 1)
        
        return t
        