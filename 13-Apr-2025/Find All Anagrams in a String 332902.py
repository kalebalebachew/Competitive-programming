# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        p_count = {}
        for c in p: p_count[c] = p_count.get(c, 0) + 1
        ans = []
        curr_count = {}
        for i in range(len(s)):
            curr_count[s[i]] = curr_count.get(s[i], 0) + 1
            if i >= len(p):
                curr_count[s[i-len(p)]] -= 1
                if curr_count[s[i-len(p)]] == 0: del curr_count[s[i-len(p)]]
            if curr_count == p_count: ans.append(i-len(p)+1)
        return ans
        
        