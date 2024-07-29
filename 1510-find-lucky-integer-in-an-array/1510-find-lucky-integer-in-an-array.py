class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        luckies = 0
        result = [-1]

        
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        
        for key, value in hashmap.items():
            if key == value:
                result.append(key)
                luckies += 1
        return max(result)
            
            

        