class Solution:
    def intToRoman(self, num: int) -> str:
        v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = []
        for v, s in zip(v, s):   
            while num >= v:
                res.append(s)
                num -= v
        return ''.join(res)
        

        #1991 -1000(M) = 991 -900(CM) = 91 - 90(XC) - 1(I)
        #3749 - 1000(M) = 2749 - 1000(M) = 1749 - 100(M) = 749 - 500(D) = 249 - 100(C) = 149 - 100(C) = 49 -40(L) = 9 - 9(X) = 0  ==== MMMDCCLX