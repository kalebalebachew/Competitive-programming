class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in ss:
                ss.remove(s[left])
                left += 1
            else:
                ss.add(s[right])

            res = max(res, right - left + 1)
        return res


     
     
        

        


            
        