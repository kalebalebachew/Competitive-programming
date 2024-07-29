class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dic = {}
        count = 0

        for char in allowed:
            dic[char] = 1

        for word in words:
            consistent = all(char in dic for char in word)
            if consistent:
                count += 1

        return count


            
