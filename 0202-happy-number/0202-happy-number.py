class Solution:
    def isHappy(self,n: int) -> bool:
        ss = set()
        while n != 1 and n > 0:
            n = sum(int(i) ** 2 for i in str(n))  
            if n in ss:
                return False
            ss.add(n)
        return True

        

        

        


        
        