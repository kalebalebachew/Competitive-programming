class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)

        check = Counter("balloon")
        minimum = float('inf')
        for k in check:
            minimum = min(minimum,c[k] // check[k])
        return minimum
                



        