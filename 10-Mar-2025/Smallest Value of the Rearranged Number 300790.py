# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        isneg = num < 0
        nu = list(str(abs(num)))
        if isneg:
            nu.sort(reverse=True)  
        else:
            nu.sort()  
            sm = -1
            for i in range(len(nu)):
                if nu[i] != '0':
                    sm = i
                    break
            if sm > 0:  
                nu[0], nu[sm] = nu[sm], nu[0]

        res = int(''.join(nu))
        if isneg:
            res = -res
        return res
            


        