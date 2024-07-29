class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        j = word.find(ch)
        result = list(word)

        while i < j:
            result[i],result[j] = result[j],result[i]
            i += 1
            j -= 1
        return "".join(result)

        

