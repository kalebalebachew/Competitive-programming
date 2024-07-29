class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

      
        common_counts = Counter(words[0])

     
        for word in words[1:]:
            word_counts = Counter(word)

            for char in common_counts:
                common_counts[char] = min(common_counts[char], word_counts[char])

        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)

        return result
               
            


        
        
        
        