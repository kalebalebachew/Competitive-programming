# Problem: 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l = 0
        c = 0
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[r])
            c = max(c, r - l + 1)
        return c
        
          