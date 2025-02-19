class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in reversed(range(len(arr))):
            curr = arr[i]
            arr[i] = mx
            mx = max(curr, mx)
        return arr

 
        