class Solution:
    def isHappy(self, n: int) -> bool:
        ss = set()
        while n != 1 and n not in ss:
            ss.add(n)
            next_n = 0
            while n > 0:
                digit = n % 10
                next_n += digit ** 2
                n //= 10
            n = next_n
        return n == 1
        

        

        


        
        