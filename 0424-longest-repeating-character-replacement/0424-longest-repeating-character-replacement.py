class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hm = Counter()
        res = 0
        longest = 0

        for right in range(len(s)):
            hm[s[right]] += 1

            longest = max(longest, hm[s[right]])

            while (right - left + 1) - longest > k:
                hm[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res





    



     


        

        