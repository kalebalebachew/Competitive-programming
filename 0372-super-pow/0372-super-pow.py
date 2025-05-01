class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for d in b:
            res = ((res ** 10) * (a**d % 1337)) % 1337
        return res