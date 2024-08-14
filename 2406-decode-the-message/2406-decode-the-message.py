class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        
        for char in key:
            if char not in dic and char != ' ':
                dic[char] = alphabet[index]
                index += 1
                if index == 26: 
                    break
        
        decoded_message = ''.join(dic.get(char, char) for char in message)
        
        return decoded_message

        
        