class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        c = Counter()
        res = 0

        for right in range(len(s)):
            c[s[right]] += 1

            longest = max(longest, c[s[right]])

            while (right - left + 1) - longest > k:
                c[s[left]] -= 1
                left += 1
            res = max(res, right - left +1)

        return res



     


        

        