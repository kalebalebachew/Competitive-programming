# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        seen = set()
        stack = []
        for c in s:
            freq[c] -= 1
            if c not in seen:
                while stack and c < stack[-1] and freq[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return ''.join(stack)