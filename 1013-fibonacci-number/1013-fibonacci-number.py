class Solution:
    def fib(self, n: int) -> int:
        k = [0,1]
        if n <= 1 :
            return n
        for i in range( 2, n+1 ):
            k.append( k[i-1] + k[i-2] )
        return k[-1]        