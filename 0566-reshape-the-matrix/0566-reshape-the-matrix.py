class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat = [num for row in mat for num in row]
        
        new_mat = []
        for i in range(r):
            new_mat.append(flat[i * c:(i + 1) * c])
        
        return new_mat
