class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        lst = [num for row in mat for num in row]
        res=[]
        for i in range(r):
            s=i*c
            e=(i+1)*c
            piece=lst[s:e]
            res.append(piece)
        return res

        