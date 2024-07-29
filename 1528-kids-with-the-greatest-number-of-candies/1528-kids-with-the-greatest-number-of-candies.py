class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= max_candy
        return candies



    


        
        