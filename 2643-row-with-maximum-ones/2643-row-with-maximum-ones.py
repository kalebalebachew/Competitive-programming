class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        br = 0
        ones = sum(mat[0])
        for i in range(1, len(mat)):
            cr = sum(mat[i])
            if cr > ones:
                ones = cr
                br = i
        return [br, ones]


        