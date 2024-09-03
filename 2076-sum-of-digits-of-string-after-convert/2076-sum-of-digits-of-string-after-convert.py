class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        for _ in range(k):
            ss = str(sum(int(digit) for digit in ss))
        
        return int(ss)


        