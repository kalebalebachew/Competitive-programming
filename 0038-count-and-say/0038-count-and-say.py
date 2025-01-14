class Solution:
    @staticmethod
    def countAndSay(n: int) -> str:
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        if n == 1:
            return "1"

        def next_sequence(s: str) -> str:
            return ''.join(str(len(list(group))) + digit for digit, group in groupby(s))

        current = "1"
        for _ in range(1, n):
            current = next_sequence(current)

        return current
        