class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        
        while n != 1 and n not in dic:
            dic[n] = True
            k = 0
            while n > 0:
                digit = n % 10
                k += digit ** 2
                n //= 10
            n = k
        
        return n == 1
        


        
        